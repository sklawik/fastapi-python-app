<template>
  All of the todos:

  <div v-if="todos.length != 0">
    <div v-for="todo in todos">
      <TodoItem :id=todo.id :title=todo.title :description= todo.description >test</TodoItem>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { todoList } from "../../services/todoService";
import TodoItem from "@/components/view/TodoItem.vue";
const todos = ref([]);

onMounted(async () => {
  todos.value = JSON.parse(await todoList());
});
</script>
