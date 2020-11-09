<template>
  <div class="header">
    <div class="nav-bar">
      <nav>
        <ul>
          <li><router-link to="home">Inicio</router-link></li>
          <li><router-link to="documents">Documentos</router-link></li>
          <li>
            <a @click="logout" class="">
              <span v-if="isAuthenticated">Salir</span
              ><span v-else>Ingresar</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
    <h1>Bienvenido: {{ getUser.email }}</h1>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "navbar",
  computed: {
    ...mapGetters("authModule", ["getUser"]),
    ...mapGetters("authModule", ["isAuthenticated"]),
  },
  methods: {
    logout: function () {
      this.$store
        .dispatch("authModule/revokeAuthToken")
        .then(() => {
          this.$router.push({ name: "login" });
        })
        .catch(() => {});
    },
  },
};
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 10%;
  background: rgb(31, 46, 45);
  height: 40px;
  margin-bottom: 20px;
}

.nav-bar {
  list-style: none;
}

.header h1 {
  color: white;
  font-size: 15px;
}

li a {
  text-decoration: none;
  color: white;
  padding: 14px 17px;
}

.nav-bar li {
  display: inline-block;
  padding: 0 20px;
  font-size: 15px;
}

.nav-bar li a span {
  display: inline-block;
  padding: 0 20px;
  font-size: 15px;
  color: white;
  cursor: pointer;
}

.nav-bar li a span:hover {
  color: paleturquoise;
  transition: all 0.4s ease 0s;
}

.nav-bar li a {
  transition: all 0.4s ease 0s;
}

.nav-bar li a:hover {
  color: paleturquoise;
  transition: all 0.4s ease 0s;
}
</style>

