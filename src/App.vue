<script setup>
const base = import.meta.env.BASE_URL
const images = Array.from({ length: 8 }, (_, i) => `${base}${i + 1}.jpg`)

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <div class="flex flex-col">
    <template v-for="(src, index) in images" :key="index">
      <!-- 第2張圖：講師陣容，加上兩個導航按鈕 -->
      <div v-if="index === 1" id="faculty" class="relative">
        <img :src="src" alt="講師陣容" class="w-full block" />
        <!-- 程潔茵 - 框框右下角按鈕 -->
        <button
          class="absolute right-4 bg-white/80 text-gray-700 text-xs px-3 py-1.5 rounded-full shadow backdrop-blur-sm cursor-pointer"
          style="top: 50%"
          @click="scrollTo('instructor-cheng')"
        >
          了解更多 ▸
        </button>
        <!-- 葉閔維 - 框框右下角按鈕 -->
        <button
          class="absolute left-4 bg-white/80 text-gray-700 text-xs px-3 py-1.5 rounded-full shadow backdrop-blur-sm cursor-pointer"
          style="top: 83%"
          @click="scrollTo('instructor-yeh')"
        >
          了解更多 ▸
        </button>
      </div>
      <!-- 第3張圖：程潔茵介紹 -->
      <div v-else-if="index === 2" id="instructor-cheng" class="relative">
        <img :src="src" alt="程潔茵 講師介紹" class="w-full block" />
        <button
          class="absolute right-4 bottom-4 bg-white/80 text-gray-700 text-xs px-3 py-1.5 rounded-full shadow backdrop-blur-sm cursor-pointer"
          @click="scrollTo('faculty')"
        >
          ◂ 回講師陣容
        </button>
      </div>
      <!-- 第4張圖：葉閔維介紹 -->
      <div v-else-if="index === 3" id="instructor-yeh" class="relative">
        <img :src="src" alt="葉閔維 講師介紹" class="w-full block" />
        <button
          class="absolute right-4 bottom-4 bg-white/80 text-gray-700 text-xs px-3 py-1.5 rounded-full shadow backdrop-blur-sm cursor-pointer"
          @click="scrollTo('faculty')"
        >
          ◂ 回講師陣容
        </button>
      </div>
      <!-- 其他圖片 -->
      <img v-else :src="src" :alt="`圖片 ${index + 1}`" class="w-full block" />
    </template>

    <div class="py-10 px-5 text-center bg-white">
      <h2 class="text-2xl font-bold text-gray-800 mb-5">想知道更多資訊嗎？</h2>
      <el-button
        type="success"
        size="large"
        round
        tag="a"
        href="https://docs.google.com/forms/d/e/1FAIpQLSeDzGj9mdnR_P8A7BJplJ8mSK6aIkLHxkqp4-_J7eZuwE0ACQ/viewform"
        class="!text-lg !px-8 !py-5"
      >
        馬上報名 ▶
      </el-button>
    </div>
  </div>
</template>
