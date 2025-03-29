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

const handleRemoveButtonClick=  async ()=>{
    let res = await fetch(`http://localhost:8000/todos?id=${props.id}`, {method: 'DELETE'})
    console.log(res)
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
