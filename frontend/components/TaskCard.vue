<script setup>
defineProps(['tarefa'])
defineEmits(['concluir','deletar'])
</script>

<template>
  <div 
    class="group mb-3 bg-white p-4 rounded-xl shadow-sm border-l-4 transition-all hover:shadow-md"
    :class="tarefa.concluida ? 'border-green-500 opacity-75' : 'border-red-400'"
  >
    <div class="flex justify-between items-center gap-3">
        <div class="flex-1">
          <h3 :class="tarefa.concluida ? 'text-gray-400 line-through' : 'text-gray-800 font-bold text-sm'">
            {{ tarefa.titulo }}
          </h3>
        </div>
      
        <button 
          v-if="!tarefa.concluida"
          @click="$emit('concluir', tarefa)"
          class="p-1.5 rounded-full bg-gray-50 text-gray-400 hover:bg-green-100 hover:text-green-600 transition-colors"
          title="Marcar como concluída"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
        </button>
        <button 
          v-if="tarefa.concluida"
          @click="$emit('deletar', tarefa)"
          class="p-1.5 rounded-full bg-gray-50 text-gray-400 hover:bg-red-100 hover:text-red-600 transition-colors"
          title="Deletar tarefa"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="3 6 5 6 21 6"></polyline>
            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            <line x1="10" y1="11" x2="10" y2="17"></line>
            <line x1="14" y1="11" x2="14" y2="17"></line>
          </svg>
        </button>

    </div>
  </div>
</template>