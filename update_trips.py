#!/usr/bin/env python3
import re, sys
FILE = 'index.html'
with open(FILE, 'r') as f:
    html = f.read()

# 1. Replace Recent Trips header
old_h = """<div style="display:flex;align-items:center;gap:10px"><span style="font-family:'Playfair Display',Georgia,serif;font-size:18px;font-weight:700;color:#0f172a">Recent Trips</span><span id="tripCount" style="padding:2px 10px;border-radius:100px;background:#f1f5f9;font-size:12px;font-weight:700;color:#64748b">0 trips</span></div>"""
new_h = """<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px"><div style="display:flex;align-items:center;gap:10px"><span style="font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:22px;font-weight:400;color:#0f172a">Recent Trips</span><span id="tripCount" style="padding:3px 12px;border-radius:100px;background:#E6F1FB;font-size:12px;font-weight:600;color:#0C447C">0 trips</span></div><button onclick="openAt()" style="display:inline-flex;align-items:center;gap:6px;padding:10px 22px;border:none;border-radius:24px;background:#16a34a;color:#fff;font-size:14px;font-weight:500;cursor:pointer">+ Add Trip</button></div>"""
if old_h in html:
    html = html.replace(old_h, new_h, 1)
    print("1. Header replaced")
else:
    print("1. SKIP header not found")

# 2. Replace periodFilters
old_pf = re.search(r'<div id="periodFilters"[^>]*>.*?</div>', html)
if old_pf:
    new_pf = '<div style="display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:12px;flex-wrap:wrap"><div style="display:flex;align-items:center;gap:16px"><div id="periodFilters" style="display:inline-flex;gap:0;border:1px solid #e2e8f0;border-radius:24px;overflow:hidden;background:#f8fafc"><button onclick="filterPeriod(\'day\')" style="padding:7px 16px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:none">Day</button><button onclick="filterPeriod(\'week\')" style="padding:7px 16px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:none">Week</button><button onclick="filterPeriod(\'month\')" style="padding:7px 16px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:none">Month</button><button onclick="filterPeriod(\'year\')" style="padding:7px 16px;font-size:12px;font-weight:600;cursor:pointer;background:#1B4DDB;color:#fff;border:none">Year</button></div><div id="periodNav" style="display:flex;align-items:center;gap:10px"><button onclick="shiftPeriod(-1)" style="width:32px;height:32px;border-radius:50%;border:1px solid #e2e8f0;background:#fff;cursor:pointer;font-size:14px;color:#64748b;display:flex;align-items:center;justify-content:center">&#8249;</button><span id="periodLabel" style="font-size:15px;font-weight:600;color:#0f172a;min-width:44px;text-align:center">2026</span><button id="periodFwd" onclick="shiftPeriod(1)" style="width:32px;height:32px;border-radius:50%;border:1px solid #e2e8f0;background:#fff;cursor:pointer;font-size:14px;color:#64748b;display:flex;align-items:center;justify-content:center">&#8250;</button></div></div><div style="display:flex;align-items:center;gap:12px">'
    html = html[:old_pf.start()] + new_pf + html[old_pf.end():]
    print("2. periodFilters replaced")
else:
    print("2. SKIP")

# 3. Replace catFilters
old_cf = re.search(r'<div id="catFilters"[^>]*>.*?</div>', html)
if old_cf:
    new_cf = '<div id="catFilters" style="display:inline-flex;gap:6px"><button onclick="filterCat(\'all\')" style="padding:7px 18px;font-size:12px;font-weight:600;cursor:pointer;background:#0f172a;color:#fff;border:none;border-radius:24px">All</button><button onclick="filterCat(\'business\')" style="padding:7px 18px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:1px solid #e2e8f0;border-radius:24px">Business</button><button onclick="filterCat(\'personal\')" style="padding:7px 18px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:1px solid #e2e8f0;border-radius:24px">Personal</button><button onclick="filterCat(\'unclassified\')" style="padding:7px 18px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;border:1px solid #e2e8f0;border-radius:24px">Unclass.</button></div><button onclick="resetPeriodToNow()" style="font-size:13px;font-weight:500;color:#1B4DDB;background:none;border:none;cursor:pointer">This Year</button></div></div>'
    html = html[:old_cf.start()] + new_cf + html[old_cf.end():]
    print("3. catFilters replaced")
else:
    print("3. SKIP")

# 4. Update filterPeriod button styles
html = html.replace(
    "b.style.background='#f1f5f9';b.style.color='#64748b';});event.target.style.background='#1B4DDB'",
    "b.style.background='transparent';b.style.color='#64748b';});event.target.style.background='#1B4DDB'", 1)
print("4. filterPeriod styles updated")

# 5. Update filterCat button styles
html = html.replace(
    "b.style.background='#f1f5f9';b.style.color='#64748b';});event.target.style.background='#0f172a';event.target.style.color='#fff';renderFilteredTrips",
    "b.style.background='transparent';b.style.color='#64748b';b.style.border='1px solid #e2e8f0';});event.target.style.background='#0f172a';event.target.style.color='#fff';event.target.style.border='none';renderFilteredTrips", 1)
print("5. filterCat styles updated")

# 6. Replace trip card template
old_card = "return '<div style=\"border:1px solid #f1f5f9;border-radius:14px;padding:16px 20px;margin-bottom:10px\">"
new_card = "return '<div style=\"border-radius:16px;border:1px solid #e2e8f0;background:#fff;overflow:hidden;margin-bottom:12px\">"
old_card_body = """<div style="display:flex;align-items:center;gap:14px"><div style="display:flex;flex-direction:column;align-items:center;gap:2px"><div style="width:10px;height:10px;border-radius:50%;border:2.5px solid '+cc+'"></div><div style="width:2.5px;height:20px;border-radius:2px;background:'+cc+'44"></div><div style="width:10px;height:10px;border-radius:50%;background:'+cc+'"></div></div><div style="flex:1"><p style="font-size:14px;font-weight:500;color:#111827;margin:0">'+t.f+' \\u2192 '+t.t+'</p><p style="font-size:12px;color:#94a3b8;margin:4px 0 0">'+dd+'</p></div><span style="font-size:11px;font-weight:500;padding:3px 12px;border-radius:100px;background:'+cb+';color:'+cc+'">'+cl+'</span><div style="text-align:right"><p style="font-family:Playfair Display,serif;font-size:24px;font-weight:700;color:#111827;margin:0">'+t.m.toFixed(1)+'</p><p style="font-size:11px;color:#94a3b8;margin:0">km</p></div>'+(t.d>0?'<span style="font-size:12px;font-weight:600;color:#16a34a">+$'+t.d.toFixed(2)+'</span>':'')+'<button onclick="deleteTrip('+_tr.indexOf(t)+')" style="background:none;border:none;font-size:16px;color:#cbd5e1;cursor:pointer">\\u00d7</button></div></div>'"""
new_card_body = """<div style="height:52px;position:relative;display:flex;align-items:center;padding:0 20px;background:linear-gradient(135deg,'+(t.c==='business'?'#E6F1FB,#B5D4F4':'#FBEAF0,#F4C0D1')+')"><div style="width:8px;height:8px;border-radius:50%;background:#0f172a;z-index:1"></div><div style="height:2px;flex:1;margin:0 4px;z-index:1;background:'+(t.c==='business'?'#1B4DDB':'#D4537E')+'"></div><span style="position:absolute;right:20px;top:8px;font-size:11px;font-weight:500;color:#475569">'+dd+'</span><span style="position:absolute;right:20px;bottom:8px;font-size:10px;font-weight:600;padding:2px 10px;border-radius:4px;text-transform:uppercase;letter-spacing:.5px;color:#fff;background:'+(t.c==='business'?'#1B4DDB':'#D4537E')+'">'+cl+'</span></div><div style="padding:16px 20px 12px"><div style="display:grid;grid-template-columns:1fr auto;gap:20px;align-items:start"><div><div style="display:flex;align-items:flex-start;gap:10px"><div style="display:flex;flex-direction:column;align-items:center;padding-top:4px"><div style="width:10px;height:10px;border-radius:50%;border:2.5px solid '+cc+'"></div><div style="width:2px;height:22px;margin:3px 0;background:'+cc+'44"></div></div><div><div style="font-size:10px;text-transform:uppercase;letter-spacing:.5px;color:#94a3b8;font-weight:500">From</div><div style="font-size:14px;font-weight:500;color:#0f172a">'+t.f+'</div></div></div><div style="display:flex;align-items:flex-start;gap:10px"><div style="display:flex;flex-direction:column;align-items:center"><div style="width:10px;height:10px;border-radius:50%;border:2.5px solid '+cc+';background:'+cc+'"></div></div><div><div style="font-size:10px;text-transform:uppercase;letter-spacing:.5px;color:#94a3b8;font-weight:500">To</div><div style="font-size:14px;font-weight:500;color:#0f172a">'+t.t+'</div></div></div></div><div style="text-align:right;padding-top:4px"><div style="font-size:32px;font-weight:500;color:#0f172a;line-height:1">'+t.m.toFixed(1)+'</div><div style="font-size:11px;color:#94a3b8;margin-top:2px">kilometers</div>'+(t.d>0?'<div style="font-size:13px;font-weight:600;color:#16a34a;margin-top:4px">+$'+t.d.toFixed(2)+'</div>':'')+'</div></div></div><div style="display:flex;align-items:center;justify-content:space-between;padding:0 20px 14px"><span style="font-size:12px;padding:4px 12px;border-radius:20px;border:1px solid #e2e8f0;color:#64748b">'+dd+'</span><button onclick="deleteTrip('+_tr.indexOf(t)+')" style="display:inline-flex;align-items:center;gap:4px;padding:6px 14px;border-radius:24px;border:1px solid #fecaca;background:transparent;font-size:12px;color:#dc2626;cursor:pointer;font-weight:500">Delete</button></div></div>'"""

if old_card in html:
    html = html.replace(old_card, new_card, 1)
    print("6a. Card wrapper replaced")
if old_card_body in html:
    html = html.replace(old_card_body, new_card_body, 1)
    print("6b. Card body replaced")
else:
    print("6b. Card body not found exactly - trying flexible match")
    # Try a regex approach
    pattern = r"<div style=\"display:flex;align-items:center;gap:14px\">.*?\\u00d7</button></div></div>'"
    match = re.search(pattern, html)
    if match:
        html = html[:match.start()] + new_card_body + html[match.end():]
        print("6b. Card body replaced via regex")
    else:
        print("6b. WARNING: Could not find card body")

with open(FILE, 'w') as f:
    f.write(html)
print(f"\nDone! Saved {FILE} ({len(html):,} bytes)")
