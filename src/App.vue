<script setup>
const images = Array.from({ length: 8 }, (_, i) => `/${i + 1}.jpg`)
</script>

<template>
  <div class="flex flex-col">
    <img
      v-for="(src, index) in images"
      :key="index"
      :src="src"
      :alt="`圖片 ${index + 1}`"
      class="w-full block"
    />

    <div class="py-10 px-5 text-center bg-white">
      <h2 class="text-2xl font-bold text-gray-800 mb-5">想知道更多資訊嗎？</h2>
      <el-button
        type="success"
        size="large"
        round
        tag="a"
        href="https://chatgpt.com/zh-TW/"
        class="!text-lg !px-8 !py-5"
      >
        點我私訊IG小編了解更多 ▶
      </el-button>
    </div>
  </div>
</template>
