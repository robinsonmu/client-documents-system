<template>
  <div class="document">
    <Navbar />
    <DocumentComponent />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import DocumentComponent from "@/components/DocumentComponent.vue";

export default {
  name: "document",
  components: {
    Navbar,
    DocumentComponent,
  },
};
</script>

