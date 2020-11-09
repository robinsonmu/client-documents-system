<template>
  <div class="card">
    <h1>Adjunte sus documentos</h1>
    <div class="form">
      <div class="card_input">
        <div class="id">
          <p>Adjunte su documento de identidad:</p>
          <input type="file" accept="pdf" />
        </div>
        <div class=""></div>
      </div>
      <button class="button">Enviar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "documentComponent",
};
</script>

<style>
.card {
  margin-top: 20px;
  width: 700px;
  height: 500px;
  border: 2px solid black;
  position: fixed;
  box-sizing: border-box;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  border-radius: 20px;
}

.card h1 {
  margin-top: 20px;
}

.card_input div {
  margin-top: 20px;
}

p {
  font-weight: bold;
}

.button {
  font-weight: bold;
  width: 100px;
  color: white;
  text-transform: uppercase;
  font-size: 0.8rem;
  background: rgb(50, 168, 155);
  border-radius: 5px;
  border: none;
  padding: 0.4rem 0;
  cursor: pointer;
  display: inline-block;
  margin-top: 300px;
}

.button:active {
  opacity: 0.7;
}
</style>

