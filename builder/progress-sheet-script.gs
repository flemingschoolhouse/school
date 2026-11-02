// Fleming Schoolhouse — progress saver. Paste into Extensions > Apps Script of a Google Sheet.
const SHEET = 'Progress';

function sheet_() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(['Kid', 'Week', 'Last saved', 'Progress', 'Answers']); }
  return sh;
}

function find_(sh, kid, week) {
  const vals = sh.getDataRange().getValues();
  for (let r = 1; r < vals.length; r++) if (vals[r][0] === kid && vals[r][1] === week) return r + 1;
  return 0;
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  const lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    const d = JSON.parse(e.postData.contents);
    const sh = sheet_();
    const row = find_(sh, d.kid, d.week) || sh.getLastRow() + 1;
    sh.getRange(row, 1, 1, 5).setValues([[d.kid, d.week, new Date(), JSON.stringify(d.progress || {}), JSON.stringify(d.answers || {})]]);
    return out_({ ok: true });
  } finally { lock.releaseLock(); }
}

function doGet(e) {
  const p = e.parameter, sh = sheet_();
  const vals = sh.getDataRange().getValues().slice(1);
  if (p.action === 'get') {
    const r = vals.find(v => v[0] === p.kid && v[1] === p.week);
    return out_({ answers: r ? JSON.parse(r[4] || '{}') : {} });
  }
  if (p.action === 'all') {
    return out_({ rows: vals.filter(v => v[1] === p.week).map(v => ({ kid: v[0], saved: v[2], progress: JSON.parse(v[3] || '{}'), answers: JSON.parse(v[4] || '{}') })) });
  }
  return out_({ ok: true });
}
