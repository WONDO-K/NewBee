<template>
  <div>
    <table class="table table-hover">
      <thead class="table-warning">
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">내용</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in store.articles.result"
        :key="article.id"
        @click="goDetail(article)">
          <th scope="row">{{ article.id }}</th>
          <td>{{ cutContent(article.title) }}</td>
          <td>{{ cutContent(article.content) }}</td>
          <td>{{ article.user }}</td>
          <td>{{ slicing(article.created_at) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()

const cutContent = (content) => {
  if (!content) return null
  return content.length > 30 ? content.slice(0, 30) + '...' : content;
}

const slicing = function (string) {
  if (!string) return null
  return string.slice(0, 10);
}

const goDetail = (article) => {
  Promise.all([store.getArticle(article.id), store.getLike(article.id)]).then(() => {
    router.push({ name: 'articleDetail', params: { id: article.id }})
  })
}

</script>

<style scoped>
tr:hover {
  cursor: pointer;
}
</style>