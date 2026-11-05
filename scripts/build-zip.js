#!/usr/bin/env node
/**
 * build-zip.js
 * Packages public/download/ into public/download.zip at build time.
 * Run with:  node scripts/build-zip.js
 */

const path = require("path");
const fs   = require("fs");
const JSZip = require("jszip");

const SRC  = path.resolve(__dirname, "../public/download");
const DEST = path.resolve(__dirname, "../public/download.zip");

function walkDir(dir, base = dir) {
  const entries = [];
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    const rel  = path.relative(base, full).replace(/\\/g, "/");
    if (fs.statSync(full).isDirectory()) {
      entries.push(...walkDir(full, base));
    } else {
      entries.push({ full, rel });
    }
  }
  return entries;
}

(async () => {
  if (!fs.existsSync(SRC)) {
    console.error(`[build-zip] Source not found: ${SRC}`);
    process.exit(1);
  }

  const zip   = new JSZip();
  const files = walkDir(SRC);
  console.log(`[build-zip] Packing ${files.length} files…`);

  for (const { full, rel } of files) {
    const data = fs.readFileSync(full);
    // Put everything inside a "download/" root folder in the zip
    zip.file(`download/${rel}`, data);
    console.log(`  + download/${rel}`);
  }

  const buf = await zip.generateAsync({
    type: "nodebuffer",
    compression: "DEFLATE",
    compressionOptions: { level: 6 },
  });

  fs.writeFileSync(DEST, buf);
  console.log(`[build-zip] Written ${(buf.length / 1024).toFixed(1)} KB → ${DEST}`);
})();
