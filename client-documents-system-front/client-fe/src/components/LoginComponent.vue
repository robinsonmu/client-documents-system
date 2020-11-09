<template>
  <div class="login-parent">
    <div id="card">
      <div id="left-card">
        <div class="image">
          <img src="@/assets/computer-login.png" alt="" />
        </div>
      </div>
      <div id="right-card">
        <div class="form">
          <h1>Bienvenido!</h1>
          <form @submit.prevent="login">
            <div>
              <input required v-model="username" type="text" />
              <label>Usuario</label>
            </div>
            <div>
              <input required v-model="password" type="password" />
              <label>Contraseña</label>
            </div>
            <button class="login-button" type="submit">Ingresar</button>
          </form>
        </div>
        <div class="info">
          <p>No tiene una cuenta? <a href="">Registrese</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginComponent",
  data() {
    return {
      username: "",
      password: "",
      incorrectCredentials: false,
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("authModule/login", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.username = "";
          this.password = "";
          this.$router.push({ name: "home" });
        })
        .catch(() => {
          console.log(this.username + " " + this.password);
          alert("Credenciales invalidas");
        });
    },
  },
};
</script>

<style>
.app-bg {
  background-image: url("~@/assets/bg.png");
  background-repeat: no-repeat;
  background-size: cover;
}

#card {
  width: 700px;
  height: 400px;
  border: 2px solid black;
  border-radius: 20px;
  position: fixed;
  box-sizing: border-box;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  transition: 0.5s;
}
#right-card {
  position: absolute;
  top: 0;
  right: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 350px;
  height: 396px;
  border-top-right-radius: 19px;
  border-bottom-right-radius: 19px;
  background: white;
}

.form {
  position: relative;
}

.form h1 {
  margin-bottom: 40px;
}

.form input {
  margin-bottom: 50px;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  border: none;
  font-size: 15px;
  border-bottom: 2px solid black;
  background: none;
}

.form input:invalid {
  box-shadow: none;
}

.form input:focus,
.form input:valid {
  background-color: transparent;
  border-color: transparent;
  border-bottom: 2px solid black;
}

.form div {
  position: relative;
  display: inline;
}

.form div label {
  position: absolute;
  top: 0px;
  left: 0;
  transition: 0.5s;
  pointer-events: none;
  color: black;
  font-size: 15px;
  display: inline-block;
}

.form input:focus ~ label,
.form input:valid ~ label {
  top: -20px;
  font-size: 13px;
  font-weight: bold;
  transition: 0.5s;
  left: 0;
}

.login-button {
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
}

.login-button:active {
  opacity: 0.7;
}

#left-card {
  position: absolute;
  left: 0;
  right: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 350px;
  height: 396px;
  border-bottom-left-radius: 19px;
  border-top-left-radius: 19px;
  background: rgb(65, 131, 153);
  background: linear-gradient(
    0deg,
    rgba(65, 131, 153, 1) 7%,
    rgba(76, 255, 231, 1) 68%
  );
}

img {
  max-width: 75%;
  max-height: 75%;
  display: inline;
  margin: 50px 0;
}

.info {
  margin-top: 30px;
  font-size: 12px;
}

.info p {
  white-space: nowrap;
}

a {
  font-weight: bold;
  text-decoration: none;
  color: black;
}
</style>
