<template>
  <div id="app">
    <h1>Busca de Operadoras de Saúde</h1>
    
    <div class="search-container">
      <input 
        type="text" 
        v-model="searchQuery" 
        @input="handleSearch" 
        placeholder="Digite o nome da operadora..."
      />
      <button @click="handleSearch">Buscar</button>
    </div>
    
    <div v-if="loading" class="loading">Carregando...</div>
    
    <div v-if="error" class="error">{{ error }}</div>
    
    <div v-if="results.length > 0" class="results">
      <h2>Resultados ({{ results.length }})</h2>
      <table>
        <thead>
          <tr>
            <th>Razão Social</th>
            <th>CNPJ</th>
            <th>Registro ANS</th>
            <th>Modalidade</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="operadora in results" :key="operadora.Registro_ANS">
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.CNPJ }}</td>
            <td>{{ operadora.Registro_ANS }}</td>
            <td>{{ operadora.Modalidade }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <div v-else-if="searchQuery && !loading" class="no-results">
      Nenhuma operadora encontrada com o termo "{{ searchQuery }}"
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      searchQuery: '',
      results: [],
      loading: false,
      error: null
    }
  },
  methods: {
    async handleSearch() {
      if (this.searchQuery.trim() === '') {
        this.results = [];
        return;
      }
      
      this.loading = true;
      this.error = null;
      
      try {
        const response = await axios.get('http://localhost:8000/buscar', {
          params: {
            query: this.searchQuery
          }
        });
        this.results = response.data;
      } catch (err) {
        this.error = 'Erro ao buscar operadoras. Verifique se o servidor está rodando.';
        console.error(err);
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.search-container {
  margin: 20px 0;
  display: flex;
  gap: 10px;
}

input {
  padding: 10px;
  font-size: 16px;
  flex-grow: 1;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #3aa876;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.loading, .error, .no-results {
  margin: 20px 0;
  padding: 10px;
  border-radius: 4px;
}

.loading {
  background-color: #f8f8f8;
  color: #666;
}

.error {
  background-color: #ffebee;
  color: #d32f2f;
}

.no-results {
  background-color: #fff8e1;
  color: #ff8f00;
}
</style>