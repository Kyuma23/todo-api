<script setup>
// 1. Configuração do URL da API (SSR + Client)
const config = useRuntimeConfig()
const apiUrl = process.server ? 'http://web:8000' : config.public.apiBase

// 2. Pedido principal à API Python
const { data: tarefas, status, error, refresh } = await useFetch('/tarefas/', {
  baseURL: apiUrl
})

// 3. Função para criar nova tarefa (Recebe o título do Header)
// Dentro do <script setup> no index.vue

const adicionarTarefa = async (dados) => {
  try {
    await $fetch('/tarefas/', {
      method: 'POST',
      baseURL: config.public.apiBase,
      body: { 
        titulo: dados.titulo, 
        descricao: dados.descricao, // Agora enviamos a descrição real!
        concluida: false 
      }
    })
    refresh() // Atualiza a lista
  } catch (err) {
    console.error("Erro ao adicionar:", err.response?._data || err)
  }
}

const concluirTarefa = async (tarefa) => {
  try {
    // Chamada PUT conforme a tua documentação
    await $fetch(`/tarefas/${tarefa.id}`, {
      method: 'PUT',
      baseURL: config.public.apiBase,
      // Enviamos a tarefa com o status invertido
      body: { 
        ...tarefa, 
        concluida: true 
      }
    })
    
    // Atualiza a lista no ecrã (as colunas Kanban movem a tarefa sozinhas)
    refresh()
  } catch (err) {
    console.error("Erro ao concluir tarefa:", err)
  }
}

const deletarTarefa = async (tarefa) => {
try {
    await $fetch(`/tarefas/${tarefa.id}`, {
      method: 'DELETE',
      baseURL: config.public.apiBase
    })
    
    refresh() 
    
  } catch (err) {
    console.error("Erro ao apagar tarefa:", err)
  }
}

// 4. Filtros para as colunas Kanban
const pendentes = computed(() => tarefas.value?.filter(t => !t.concluida) || [])
const concluidas = computed(() => tarefas.value?.filter(t => t.concluida) || [])
</script>

<template>
  <div class="p-8 max-w-6xl mx-auto min-h-screen">
    
    <KanbanHeader @add="adicionarTarefa" />

    <div v-if="status === 'pending'" class="text-center py-10 text-gray-500 animate-pulse">
      A ligar ao servidor Python...
    </div>

    <div v-else-if="error" class="bg-red-50 text-red-600 p-4 rounded-lg text-center border border-red-100">
      Não foi possível carregar as tarefas. Verifica se a API está ativa.
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-10">
      
      <section class="flex flex-col">
        <div class="flex items-center justify-between mb-4 px-2">
          <h2 class="font-bold text-gray-600 uppercase text-sm tracking-widest">A Fazer</h2>
          <span class="bg-gray-200 text-gray-700 text-xs font-bold px-2 py-1 rounded-md">
            {{ pendentes.length }}
          </span>
        </div>
        
        <div class="space-y-4">
          <TaskCard 
            v-for="t in pendentes" 
            :key="t.id" 
            :tarefa="t" 
            @concluir="concluirTarefa" 
          />
          <p v-if="pendentes.length === 0" class="text-center py-10 border-2 border-dashed rounded-xl text-gray-400 italic text-sm">
            Tudo em dia! ✨
          </p>
        </div>
      </section>

      <section class="flex flex-col">
        <div class="flex items-center justify-between mb-4 px-2">
          <h2 class="font-bold text-green-700 uppercase text-sm tracking-widest">Feito</h2>
          <span class="bg-green-100 text-green-700 text-xs font-bold px-2 py-1 rounded-md">
            {{ concluidas.length }}
          </span>
        </div>

        <div class="space-y-4">
          <TaskCard v-for="t in concluidas" :key="t.id" :tarefa="t" @deletar="deletarTarefa"/>
          <p v-if="concluidas.length === 0" class="text-center py-10 border-2 border-dashed border-gray-200 rounded-xl text-gray-400 italic text-sm">
            Nada concluído ainda.
          </p>
        </div>
      </section>

    </div>
  </div>
</template>