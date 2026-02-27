<script setup>
defineEmits(['exit-dev'])
</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 text-center">
    <!-- 動畫圖示 -->
    <div class="relative mb-8">
      <div class="w-32 h-32 rounded-full bg-emerald-100 flex items-center justify-center animate-pulse-slow">
        <svg class="w-16 h-16 text-emerald-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>
      </div>
      <!-- 裝飾小點 -->
      <span class="absolute top-0 right-0 w-4 h-4 bg-teal-300 rounded-full animate-bounce-slow" />
      <span class="absolute bottom-2 -left-2 w-3 h-3 bg-emerald-300 rounded-full animate-bounce-slow-delay" />
    </div>

    <!-- 主標題 -->
    <h1 class="text-3xl font-bold text-gray-800 mb-3">頁面準備中</h1>
    <p class="text-gray-500 text-lg mb-2 max-w-xs">此頁面尚未開放，敬請期待</p>
    <p class="text-gray-400 text-sm mb-10">我們正在努力建置中，很快就會與您見面！</p>

    <!-- 分隔裝飾 -->
    <div class="flex items-center gap-2 mb-10">
      <span class="w-8 h-px bg-emerald-300" />
      <span class="w-2 h-2 rounded-full bg-emerald-400" />
      <span class="w-8 h-px bg-emerald-300" />
    </div>

    <!-- 健康班 Logo 文字 -->
    <p class="text-emerald-600 font-semibold tracking-widest text-sm">健康班 WellnessFlow</p>
  </div>
</template>

<style scoped>
@keyframes pulse-slow {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.85; }
}
@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
@keyframes bounce-slow-delay {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}
.animate-pulse-slow {
  animation: pulse-slow 3s ease-in-out infinite;
}
.animate-bounce-slow {
  animation: bounce-slow 2s ease-in-out infinite;
}
.animate-bounce-slow-delay {
  animation: bounce-slow-delay 2.5s ease-in-out 0.5s infinite;
}
</style>
