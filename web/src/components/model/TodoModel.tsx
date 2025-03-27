export const  todoList =  async  function () {

  const data = await fetch("http://localhost:8000/todos");
  const todoList = await data.text()
  return todoList;
}
