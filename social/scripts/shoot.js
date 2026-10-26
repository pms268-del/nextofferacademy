// Screenshot every .slide element in an HTML file to PNG.
// Usage: node shoot.js <input.html> <outDir> <prefix>
const path = require('path');
const { chromium } = require('playwright');

async function main() {
  const [, , input, outDir, prefix] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    const n = String(i + 1).padStart(2, '0');
    await slides[i].screenshot({ path: path.join(outDir, `${prefix}_${n}.png`) });
  }
  console.log(`${slides.length} slides -> ${outDir}/${prefix}_NN.png`);
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
