<template>
  <div class="container">
    <div class="jumbotron">
      <h1 class="display-4">Kazıklanmadım :)</h1>
      <hr class="my-4" />

      <p class="lead">
        Aldığın ürünün ismini yaz ve en ucuz fiyatı gör :) (eti cicibebe).
      </p>
      <input
        class="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
        v-model="searchVariable"
      />
      <br />
      <button @click="search" class="btn btn-primary" type="submit">
        Search
      </button>
    </div>

    <br />

    <div v-for="(data, index) in datas" :key="index">
      {{ index }}
      <br />
      {{ data }} TL
      <br />
      <br />
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Main",

  data() {
    return {
      searchVariable: "",
      datas: {},
    };
  },

  methods: {
    search() {
      this.datas = {};
      let url = "http://localhost:8000/" + this.searchVariable;
      axios
        .get(url)
        .then((response) => {
          this.datas = response.data;
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
