"""Build the public journal from reviewed, non-sensitive content only."""
import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "docs"
e = html.escape


def build():
    data = json.loads((ROOT / "prints.json").read_text())
    cards = []
    ids = set()
    for p in data["prints"]:
        assert p["id"] not in ids, "Duplicate print ID"
        ids.add(p["id"])
        assert len(p["notes"]) == 3
        photos = p["photos"]
        for photo in photos:
            assert Path(photo["file"]).name == photo["file"]
            assert (PUBLIC / "images" / photo["file"]).is_file()
        first = photos[0]
        thumbs = "".join(
            f'<button class="thumbnail" type="button" aria-label="View photo {i + 1}: {e(photo["caption"])}" '
            f'aria-pressed="{str(i == 0).lower()}" data-src="images/{e(photo["file"])}" '
            f'data-alt="{e(photo["alt"])}" data-caption="{e(photo["caption"])}">'
            f'<img src="images/{e(photo["file"])}" alt="" width="70" height="70" loading="lazy"></button>'
            for i, photo in enumerate(photos)
        )
        settings = "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in p["settings"])
        notes = "".join(f'<li><span>{e(k)}</span><p>{e(v)}</p></li>' for k, v in p["notes"])
        cards.append(f'''
        <article class="print" id="{e(p['id'])}">
          <div class="photo-column">
            <button class="main-photo" type="button" aria-label="Enlarge photo of {e(p['object'])}">
              <img src="images/{e(first['file'])}" alt="{e(first['alt'])}" width="961" height="1280" loading="lazy">
              <span class="enlarge" aria-hidden="true">View full photo ↗</span>
            </button>
            <div class="photo-controls"><div class="thumbnails" role="group" aria-label="{e(p['object'])} photos">{thumbs}</div>
            <span class="photo-count">{len(photos)} photographs</span></div>
            <p class="caption">{e(first['caption'])}</p>
          </div>
          <div class="print-details">
            <div class="entry-meta"><span>No. {e(p['number'])} / {e(p['category'])}</span><time datetime="{p['date']}">{date.fromisoformat(p['date']).strftime('%d %b %Y')}</time></div>
            <h3>{e(p['name'])}</h3>
            <p class="object-name">{e(p['object'])} <span>·</span> {e(p['material'])}</p>
            <p class="description">{e(p['description'])}</p>
            <dl class="settings">{settings}</dl>
            <p class="estimate-note">{e(p['estimateNote'])}</p>
            <ul class="notes">{notes}</ul>
            <p class="credit">{e(p['credit'])}</p>
          </div>
        </article>''')
    count = len(cards)
    output = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Huzaifa’s personal 3D printing journal. Real prints, honest notes, and small discoveries along the way.">
  <meta name="theme-color" content="#f5f2eb">
  <title>{e(data['title'])}</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <script src="journal.js" defer></script>
</head>
<body>
  <a class="skip" href="#collection">Skip to the prints</a>
  <header class="site-header wrap">
    <a class="brand" href="#" aria-label="Huzaifa’s Print Journal home"><span class="brand-mark" aria-hidden="true">h.</span><span>Huzaifa’s<br><strong>print journal</strong></span></a>
    <a class="nav-link" href="#collection">The collection <span aria-hidden="true">↙</span></a>
  </header>
  <main>
    <section class="hero wrap" aria-labelledby="hero-title">
      <div class="hero-copy"><p class="eyebrow"><span class="dot"></span> A personal making journal</p>
        <h1 id="hero-title">Small prints.<br><em>Little discoveries.</em></h1>
        <p class="intro">A growing collection of things I’ve made, what worked, and what I’ll try next. One layer at a time.</p>
        <a class="primary-link" href="#collection">Explore the prints <span aria-hidden="true">↓</span></a>
        <div class="hero-facts"><div><strong>{count:02d}</strong><span>prints & counting</span></div><div><strong>A1</strong><span>Bambu Lab printer</span></div><div><strong>2026</strong><span>the year it began</span></div></div>
      </div>
      <figure class="hero-image"><img src="images/benchy-desk.jpg" alt="A tiny white Benchy boat on a wave-patterned desk mat beside a keyboard" width="1280" height="720" fetchpriority="high"><figcaption><span>Where it all began</span><span>Print No. 01</span></figcaption></figure>
    </section>
    <section class="collection wrap" id="collection" aria-labelledby="collection-title">
      <div class="section-heading"><div><p class="eyebrow">The collection</p><h2 id="collection-title">Made. Tested. Noted.</h2></div><p>Latest prints first.<br>Real photos. Lessons worth keeping.</p></div>
      {''.join(cards)}
    </section>
    <aside class="next-note wrap" aria-labelledby="next-title"><span class="next-icon" aria-hidden="true">↗</span><div><p class="eyebrow">On the workbench · not printed yet</p><h2 id="next-title">Same scraper. Smaller layers.</h2><p>Next experiment: compare 0.20 mm and 0.10 mm layers side by side. A closer look at finish, print time, and what actually changes.</p></div></aside>
  </main>
  <footer class="wrap"><p>Huzaifa’s print journal <span>·</span> Made with curiosity.</p><p>Updated {date.fromisoformat(data['updated']).strftime('%d %b %Y')}</p></footer>
  <dialog id="photo-viewer" aria-label="Enlarged print photograph"><button class="close-viewer" type="button" aria-label="Close photograph">Close ×</button><img alt=""><p></p></dialog>
</body>
</html>
'''
    (PUBLIC / "index.html").write_text("\n".join(line.rstrip() for line in output.splitlines()) + "\n")
    print(f"Built {count} print entries in docs/index.html")


if __name__ == "__main__":
    build()
