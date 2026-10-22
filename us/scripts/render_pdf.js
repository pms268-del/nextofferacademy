// Render an HTML file to a US Letter PDF with Chromium (Playwright).
// Usage: node render_pdf.js <input.html> <output.pdf> [--footer "Title"] [--no-footer]
const path = require('path');
const { chromium } = require('playwright');

async function main() {
  const [, , input, output, ...rest] = process.argv;
  const noFooter = rest.includes('--no-footer');
  const titleIdx = rest.indexOf('--footer');
  const title = titleIdx >= 0 ? rest[titleIdx + 1] : '';

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });

  const footer = `
    <div style="width:100%; font-family: Inter, sans-serif; font-size:7.5px; color:#5b6b82;
                padding:0 16mm; display:flex; justify-content:space-between;">
      <span>${title}</span>
      <span><span class="pageNumber"></span></span>
    </div>`;

  await page.pdf({
    path: output,
    format: 'Letter',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: !noFooter,
    headerTemplate: '<div></div>',
    footerTemplate: noFooter ? '<div></div>' : footer,
    margin: noFooter ? { top: '0', bottom: '0', left: '0', right: '0' }
                     : { top: '16mm', bottom: '16mm', left: '16mm', right: '16mm' },
    outline: true,
    tagged: true,
  });
  await browser.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
