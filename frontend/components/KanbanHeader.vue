<script setup>
import { ref, computed } from 'vue'
const titulo = ref('')
const descricao = ref('')
const isExpanded = ref(false)

const emit = defineEmits(['add'])

const submeter = () => {
  if (titulo.value.trim()) {
    emit('add', { 
      titulo: titulo.value, 
      descricao: descricao.value 
    })
    titulo.value = ''
    descricao.value = ''
    isExpanded.value = false
  }
}

const cancelar = () => {
  isExpanded.value = false
  titulo.value = ''
  descricao.value = ''
}
</script>

<template>
  <header class="max-w-sm mx-auto mb-8">
    <h1 class="text-5xl font-black text-center text-gray-800 mb-4 tracking-tighter italic">
      MY<span class="text-green-500 text-2xl">TODO</span>
    </h1>

    <div 
      class="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden transition-all duration-300"
      :class="isExpanded ? 'ring-2 ring-green-400' : ''"
    >
      <input 
        v-model="titulo"
        type="text" 
        placeholder="Nova tarefa..." 
        class="w-full px-4 py-2.5 outline-none text-gray-800 font-semibold text-sm"
        @focus="isExpanded = true"
      />

      <div 
        v-show="isExpanded" 
        class="px-4 pb-3 space-y-2 border-t border-gray-50 pt-2"
      >
        <textarea 
          v-model="descricao"
          placeholder="Detalhes..." 
          class="w-full h-16 p-0 outline-none text-gray-500 text-xs resize-none bg-transparent"
        ></textarea>

        <div class="flex gap-2 justify-end">
          <button 
            @click="cancelar"
            class="px-3 py-1 text-xs font-medium text-gray-400 hover:text-gray-600"
          >
            Cancelar
          </button>
          <button 
            @click="submeter"
            class="bg-green-500 hover:bg-green-600 text-white px-4 py-1.5 rounded-lg text-xs font-bold shadow-sm transition-all active:scale-95"
          >
            Guardar
          </button>
        </div>
      </div>
    </div>
  </header>
</template>