<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  title: String,
  description: String,
  id: String
});

const toggleStatus = () => {
  emit("toggle");
};

const handleRemoveButtonClick=  ()=>{
    
}

</script>

<template>
  <div class="todo-item">
    <div>id: {{ props.id }}</div>
    <div>{{ props.title }}</div>
    <div>{{ props.description }}</div>
    <button @click="handleRemoveButtonClick">remove</button>
  </div>
</template>

<style scoped></style>
