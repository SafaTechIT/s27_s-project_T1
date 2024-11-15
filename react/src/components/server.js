// server.js
const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000; // پورت مشخص یا 5000

// میزبانی فایل‌های استاتیک
app.use(express.static(path.join(__dirname, 'build')));

// رندر صفحه اصلی
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// راه‌اندازی سرور
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});