<template>
  All of the todos:

  <div v-if="todos.length != 0">
    <div v-for="todo in todos">
      <div class="flex flex-col w-20 gap-2 bg-red-500">
        {{ todo.title }}
        {{ todo.description }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { todoList } from "../model/TodoModel";

const todos = ref([]);

onMounted(async () => {
  todos.value = JSON.parse(await todoList());
  console.log(await todoList());
});

</script>
