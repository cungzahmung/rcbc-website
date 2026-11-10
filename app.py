"""
Raleigh Chin Baptist Church - Website (Python / Flask)
=========================================================
Run / Tuah ning:
    pip install flask
    python raleigh-chin-baptist-church-website.py
    Browser ah http://127.0.0.1:5000 hun

Pages / Cahmai:
    Home, Directory, Church Event (a chungah department
    event: Bupi, Youth, CE, Mission, Nubu), Church Leaders,
    Church News, Pathian Bia, Caan Ngeitu
    - Event page pakhat cio ah Calendar a tel.
    - Directory ah min le address in kawl khawh a si.

Edit: A tanglei DATA hrampi kha na duh ningin thlen.
Directory data cu SQLite (church_directory.db) ah a um lai,
website na restart zongah a tlau lo.

Church News / Khrihfabu thawng:
    Thawngthanh ding tial na duh cun "Thawng Thar Chiah / Add News" form ah
    Title, Date le Thawngthanh (body) tial law "Add News" hmet.
    News cu SQLite (church_directory.db, news table) ah a um lai,
    website na restart zongah a tlau lo. Delete zong page
    chung khan tuah khawh a si.

Events / Bupi, Youth, CE Event:
    An mah le department cio event page cio
    (Bupi / Youth / CE) ah a tanglei "Event Thar Chiah / Add Event"
    form ah Date, Title, Time, Place le Note tial law "Add Event"
    hmet - na thim mi ni kha calendar ah mark a si lai, note
    zong a lang lai. Event cu SQLite (church_directory.db,
    events table) ah a um lai, website na restart zongah a
    tlau lo. Delete zong page chung khan tuah khawh a si.
    Calendar a tang lei ah "Tuthla a Biapi mi Ni" table pakhat
    a um - na zoh lio mi thla i event vialte ni ningin an lang.

Church Leaders / Khrihfabu Hruaitu:
    Khrihfabu hruaitu upa pawl an min cu website ah /church-leaders page
    hun law, a tanglei "Leader Thar Chiah / Add Leader" form ah
    Min (Name), Position, Phone, Email, Bio le Picture (photo
    upload) chiah law "Add Leader" hmet. Leader cu SQLite
    (church_directory.db, leaders table) ah a um lai, website
    na restart zongah a tlau lo. Edit le Delete zong page
    chung khan tuah khawh a si - Edit ah picture thlen / hloh
    zong a ngah. Photo cu leaders table chungah BLOB in a um.

Mobile / Phone in Zoh Khawh:
    Page vialte cu phone (mobile) zongah ttha tein an lang -
    menu, calendar, table, leader photo le form vialte
    phone screen te ah an i rem (responsive). Table ngan
    pawl cu phone ah vorhlei-zanglei in na swipe khawh;
    calendar cu a tet deuh in a lang i event a lang rih.
    Computer zongah a hlun ning cun a lang rih.

Admin Login / Admin Lawngin Edit Khawh:
    Page vialte cu public nih an zoh / rel khawh - asinain
    an EDIT khawh lo. Add / Edit / Delete cu Admin lawngin
    a ngah: menu ah "Admin Login" hmet law username le
    password in lut; na edit dih ah "Logout" hmet.
    Username default: admin
    Password default: rcbc@2026
    PASSWORD THLEN NA DUH AH: code chungah ADMIN_PASSWORD
    kha na duh mi in thlen, asilole (Render caah a him bik)
    Render Dashboard > Environment ah ADMIN_PASSWORD le
    SECRET_KEY kha chiah - GitHub ah na password taktak
    cu tial hlah.

Admin Users / Admin Dang (User 5):
    Super Admin (username: admin) telh lo in, admin dang
    mi 5 tiang an um khawh: Pastor, Chairman, Secretary,
    Youth Director, C.E Director. Anmah nih admin nih a
    ngeih mi edit nawl (Add / Edit / Delete) vialte an
    ngeih ve. Account ser ning: /register page ah a mah le
    Rian (role) thim, a mah le Username le Password a duh
    ningin a ser (Super Admin nih a set piak lo); mi dang
    nih an ser sual lo nak ding Registration Code a hau -
    code cu Super Admin lawngin a theih i, mi 5 hna lawng
    a chimh hna. Code default: RCBC2026 (Super Admin nih
    /admin-users page in a thlen khawh). Super Admin nih
    /admin-users page in user account a delete piak khawh;
    Super Admin account cu delete khawh a si lo. User nih
    a password cu /change-password in amah tein a thlen
    khawh. Password cu hash in a him tein a um (a tial
    ningin a um lo).

Pathian Bia / Thawngtha Bia:
    Pathian bia/Thawngtha bia na duh ah cun, website ah /pathian-bia page
   ong law, Admin in lut law "Pathian Bia Thar Chiah / Add
    Scripture" form ah Title le Cabia (Pathian bia pumpi)
    tial - cabia box cu a ngan i, na tial pah ah amah tein
    a khat chin (auto-expand) lai. Scripture cu SQLite
    (church_directory.db, scriptures table) ah a um lai,
    website na restart zongah a tlau lo. Edit le Delete
    zong page chung khan tuah khawh a si.

Caan Ngeitu / Service Duty Roster:
    Code chungah tial hau lo in, website ah /caan-ngeitu page
    hun law, Admin in lut law "Pumhnak Thar Chiah / Add
    Service" form ah Ni (Date) le Pumhnak Lu (Title - e.g.
    "Sunday Pumhnak", "Friday zan Pumhnak") thim law, a
    tangah Rian (role) le A Ngeitu (person) tlar kha na duh
    zat tial - "Tlar Thar Chap / Add Row" in tlar chap
    khawh a si, rian zong pumhnak cio ningin a dang khawh
    (Sunday le Friday zan rian an i dang). Public page ah
    pumhnak pakhat cio cu bulletin ningin a lang: Date +
    Title lu, a tangah col hnih table (vorhlei = Rian,
    zanglei = A Ngeitu). Service cu SQLite (services le
    service_items tables) ah an um lai, restart zongah an
    hlorh lo. Edit ah tlar thar chap / hlun hloh zong a ngah.
    Khrihfabu pumhnak cu zarhkhat ah pahnih a si: Friday zan
    7:00 PM le Sunday 1:00 PM - 3:00 PM. Caan Ngeitu cu hi
    pumhnak pahnih hrambunh in a i rem - pumhnak pakhat cio
    cu a Ni (date) in a lang (e.g. Friday Nov 6, 2026;
    Sunday Nov 8, 2026). Zarh tin update nuam nak ding:
    Admin in lut law, service card chung i Quick Edit kha
    hun, min pawl kha a thlen colh law "Save / Fim" hmet -
    code va tial hau lo, page dang va hun hau lo.
    Pumhnak caan zong code chungah tial a si lo: Friday caan
    (default 7:00 PM) le Sunday caan (default 1:00 PM -
    3:00 PM) cu SQLite settings table ah an um i, Admin nih
    /caan-ngeitu page i "Pumhnak Caan / Service Times" form
    in a thlen khawh - thlen colh cun Home page, Caan Ngeitu
    page le service card vialte ah caan thar a lang colh.

Directory - Family Members / Chungtel Min:
    Family tam deuh caah Directory Add form ah "Family
    Members / Chungtel Min" tial nak a um: chungtel pakhat
    cio caah tlar pakhat ah min pakhat tial, "+ Member Thar
    Chap / Add Family Member" hmet in tlar a tam deuh zong
    chap khawh a si (a lawng mi tlar cu save a si lo).
    Table ah chungtel min cu tlar ningin an lang i, an zat
    zong a lang; chungtel min pakhat in zong Directory
    kawl (search) khawh a si. Admin nih Edit in chungtel
    min a chap / a thlen / a hloh khawh. Members cu SQLite
    (church_directory.db, members table, family_members
    column) ah an um lai - hlun DB zongah column cu amah
    tein a lut lai, data hlun a hlorh lo.

Website Design:
    Chin Bethel Church website bantukin a dawh deuh nak
    ding: Google Fonts (Montserrat + Outfit), Home ah
    hero section (logo, motto bia, service caan chip,
    a ra lai mi service donh nak COUNTDOWN - Ni,
    Suimilam, Minute, Second a nung in a kal), card
    shadow, rangkachak (gold) hri, button pill design.
    Countdown cu Service Times (Caan Ngeitu page ah
    admin nih a thlen khawh mi) a zulh ve lai.

Church News i Gallery + YouTube + About Us:
    Church News page tangah "Church Activity Pictures"
    gallery a um - admin nih hmanthlak upload/delete
    a tuah khawh. "RCBC YouTube" section ah admin nih
    channel link a save khawh i video link a chiah
    mi cu website chungah zoh khawh (embed) in a lang.
    About Us page (/about) ah khrihfabu kong tial mi
    cu admin nih website cungin a edit khawh (settings
    'about_text' ah a um).

Day / Night Mode:
    Page vialte cung ah menu donghnak i "Night" button in
    a mui mi (dark) mode ah thlen khawh a si; "Day" in a
    ceu mi ah a kir than. Na thim mi cu browser ah a um
    lai (localStorage) - page dang na kal zongah, a ra
    than tik zongah na thim mi ningin a lang lai.

Church Logo / Watermark:
    Church logo cu website page vialte background ah
    watermark (a sen lo, a hngal lo ning) in a lang lai.
    RCBC logo (Grace nih a kuat mi) cu code chungah default
    in a um cang - website run colh ah watermark a lang lai,
    upload hau lo. A hrangmi (white) background cu
    transparent ah thlen a si i, a kuang (emblem) lawng a lang;
    a tanglei Bible cafang (John 8:32 verse) cu watermark ah
    a tel lo - asinain Home page Welcome tangah RCBC motto
    "John 8:32" in a lang. Logo thlen na duh ahcun Admin in
    lut law Home page tanglei "Church Logo" card ah a dang
    upload; a lang duh lo ahcun "Logo Hloh / Remove Logo"
    hmet - delete a si ahcun default zong a kir ti lai lo.
    Logo cu SQLite (church_directory.db, site_assets table)
    ah a um lai, restart zongah a tlau lo.
"""

import base64
import binascii
import calendar as cal_module
import hashlib
import hmac
import io
import mimetypes
import os
import sqlite3
from datetime import date, timedelta
from functools import wraps

from flask import (Flask, g, redirect, render_template_string, request,
                   send_file, session, url_for)

app = Flask(__name__)
DATABASE = os.environ.get(
    "RCBC_DB_PATH",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "church_directory.db"),
)

# ------------------------------------------------------------------
# ADMIN LOGIN - Admin lawngin edit khawh
# Public cu page vialte an zoh khawh, asinain Add / Edit /
# Delete an tuah kho lo. Edit duh ah /login in lut a hau.
# Render ahcun Environment Variable in chiah (a him bik):
#   ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY
# ------------------------------------------------------------------
app.secret_key = os.environ.get("SECRET_KEY", "rcbc-change-this-secret-key")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    PERMANENT_SESSION_LIFETIME=timedelta(days=7),
)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "rcbc@2026")

# Church logo default (watermark): Grace nih a kuat mi RCBC logo
# (a kuang lawng, a hintermi background cu transparent). Website
# hramthawk ah site_assets ah a lut lai; Home page Logo card in
# a dang upload khawh a si, delete a si ahcun a lang ti lai lo.
DEFAULT_LOGO_B64 = (
    "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"
)


def is_admin():
    """Atu lutt u admin a si maw? (session in check)"""
    return session.get("admin_logged_in") is True


# Admin dang (user) rian - mi 5 lawng, rian pakhat ah account pakhat
ADMIN_ROLES = ["Pastor", "Chairman", "Secretary", "Youth Director",
               "C.E Director"]
DEFAULT_REGISTER_CODE = "RCBC2026"


def is_super_admin():
    """Atu lutt u Super Admin (username admin) a si maw?"""
    return session.get("admin_super") is True


def _hash_password(password):
    """Password kha him tein hash (salt telh in)."""
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 120000)
    return salt.hex() + "$" + dk.hex()


def _check_password(password, stored):
    try:
        salt_hex, hash_hex = (stored or "").split("$", 1)
        dk = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), bytes.fromhex(salt_hex), 120000)
        return hmac.compare_digest(dk.hex(), hash_hex)
    except Exception:
        return False


@app.context_processor
def inject_admin():
    # Template vialte ah is_admin a um - edit form / button
    # pawl cu admin lawngah lang ter, public ah thuh.
    return {"is_admin": is_admin(), "has_logo": has_logo(),
            "footer_text": get_footer_text(),
            "is_super": is_super_admin(),
            "admin_label": session.get("admin_label", "")}


def has_logo():
    """Church logo a um cang maw? (watermark lang nak ding)"""
    try:
        db = get_db()
        row = db.execute(
            "SELECT LENGTH(data) FROM site_assets WHERE key='logo'"
        ).fetchone()
        return bool(row and row[0])
    except Exception:
        return False


def _safe_next(value):
    """Login hnu kir nak address - site chung lawng a ngah."""
    if value and value.startswith("/") and not value.startswith("//"):
        return value
    return "/"


def login_required(view):
    """Edit-only route khar: admin a si lo ah login page ah kuat."""

    @wraps(view)
    def wrapped(*args, **kwargs):
        if not is_admin():
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped

# ------------------------------------------------------------------
# EDIT HERE / HI KA HIN THLENG - Church info
# ------------------------------------------------------------------
CHURCH = {
    "name": "Raleigh Chin Baptist Church",
    "tagline": "Welcome to Raleigh Chin Baptist Church",
    "address": "",   # e.g. "Raleigh, NC"
    "phone": "",
    "email": "",
    "service_time": "",  # e.g. "Sunday Worship: 1:00 PM"
    "motto": "And ye shall know the truth, and the truth shall make you free.",
    "motto_ref": "John 8:32",
}

# Church Leaders - Atu cu code chungah tial hau lo zong a ngah.
# Website ah /church-leaders page i form in Min, Position, Phone,
# Email, Bio le Picture (photo) chiah khawh a si - leader cu
# SQLite leaders table ah a um lai.
# A tanglei LEADERS cu hramthawk (seed) ca lawng a si - leaders
# table a lawng ahcun voi khat chungah an lut lai; a hnu cu
# website form in chiah mi lawng. Photo cu website form lawng
# in chiah khawh a si (code seed ah photo a um lo).
# Example format: {"name": "min", "role": "Pastor", "phone": "", "email": ""}
LEADERS = []

# Church News - Atu cu code chungah tial hau lo.
# Website ah /church-news page i form in chiah khawh a si
# (Title, Date, Thawngthanh/body). A tanglei NEWS cu hramthawk
# (seed) ca lawng a si - news table a lawng ahcun voi khat
# chungah an lut lai; a hnu cu website form in chiah mi lawng.
# Example format: {"date": "2026-11-08", "title": "Thawngthanh", "body": "..."}
NEWS = []

# Events - Atu cu code chungah tial hau lo zong a ngah.
# Event page pakhat cio i form in Date, Title, Time, Place, Note
# tialin chiah khawh a si - calendar ah mark a si lai.
# A tanglei dict pawl cu code in chiah duh ca lawng an si rih;
# website form in chiah mi cu SQLite events table ah an um lai,
# pahnih ningin calendar le table ah an lang lai.
# Format: "YYYY-MM-DD": [{"title": "...", "time": "...", "place": "...", "note": ""}]
BUPI_EVENTS = {}
YOUTH_EVENTS = {}
CE_EVENTS = {}
MISSION_EVENTS = {}
NUBU_EVENTS = {}

# ------------------------------------------------------------------
# Directory database (SQLite)
# ------------------------------------------------------------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            family TEXT DEFAULT '',
            family_members TEXT DEFAULT '',
            note TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT DEFAULT '',
            date TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            time TEXT DEFAULT '',
            place TEXT DEFAULT '',
            note TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS leaders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            email TEXT DEFAULT '',
            bio TEXT DEFAULT '',
            photo_data BLOB DEFAULT NULL,
            photo_mimetype TEXT DEFAULT '',
            sort_order INTEGER DEFAULT 0
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS scriptures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT DEFAULT '',
            date TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_date TEXT NOT NULL DEFAULT '',
            service_type TEXT DEFAULT '',
            title TEXT NOT NULL,
            note TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS service_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_id INTEGER NOT NULL,
            role TEXT DEFAULT '',
            person TEXT DEFAULT '',
            sort_order INTEGER DEFAULT 0
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT '',
            created TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS site_assets (
            key TEXT PRIMARY KEY,
            data BLOB DEFAULT NULL,
            mimetype TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS gallery_photos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caption TEXT DEFAULT '',
            data BLOB DEFAULT NULL,
            mimetype TEXT DEFAULT '',
            created TEXT DEFAULT ''
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT DEFAULT '',
            url TEXT DEFAULT '',
            video_id TEXT DEFAULT '',
            created TEXT DEFAULT ''
        )
        """
    )
    db.executemany(
        "INSERT OR IGNORE INTO settings (key, value) VALUES (?,?)",
        [("friday_time", "7:00 PM"), ("sunday_time", "1:00 PM - 3:00 PM"),
         ("register_code", DEFAULT_REGISTER_CODE)],
    )
    # Seed: code chung default logo kha site_assets ah lut ter -
    # logo a um lo i admin nih a rak delete cang lo ah lawng.
    try:
        _has_logo = db.execute(
            "SELECT LENGTH(data) FROM site_assets WHERE key='logo'"
        ).fetchone()
        _disabled = db.execute(
            "SELECT value FROM settings WHERE key='logo_disabled'"
        ).fetchone()
        if (not _has_logo or not _has_logo[0]) \
                and not (_disabled and _disabled[0]) and DEFAULT_LOGO_B64:
            db.execute(
                "INSERT OR REPLACE INTO site_assets (key, data, mimetype) "
                "VALUES ('logo',?,?)",
                (base64.b64decode(DEFAULT_LOGO_B64), "image/png"),
            )
    except Exception:
        pass
    _cols = [r[1] for r in db.execute(
        "PRAGMA table_info(services)").fetchall()]
    if _cols and "service_type" not in _cols:
        db.execute(
            "ALTER TABLE services ADD COLUMN service_type TEXT DEFAULT ''")
    # Migration: a hlun members table ah family_members column
    # a um lo ahcun chap - data hlun a tlau lo in.
    _mcols = [r[1] for r in db.execute(
        "PRAGMA table_info(members)").fetchall()]
    if _mcols and "family_members" not in _mcols:
        db.execute(
            "ALTER TABLE members ADD COLUMN family_members TEXT DEFAULT ''")
    # Seed: code chung NEWS list in a voikhatnak lawng lut ter
    count = db.execute("SELECT COUNT(*) FROM news").fetchone()[0]
    if count == 0 and NEWS:
        db.executemany(
            "INSERT INTO news (title, body, date) VALUES (?,?,?)",
            [(n.get("title", ""), n.get("body", ""), n.get("date", ""))
             for n in NEWS if n.get("title")],
        )
    # Seed: code chung LEADERS list in a voikhatnak lawng lut ter
    count_l = db.execute("SELECT COUNT(*) FROM leaders").fetchone()[0]
    if count_l == 0 and LEADERS:
        db.executemany(
            "INSERT INTO leaders (name, position, phone, email, bio, sort_order) "
            "VALUES (?,?,?,?,?,?)",
            [(p.get("name", ""), p.get("role", p.get("position", "")),
              p.get("phone", ""), p.get("email", ""), p.get("bio", ""),
              p.get("sort_order", idx))
             for idx, p in enumerate(LEADERS) if p.get("name")],
        )
    db.commit()
    db.close()


# ------------------------------------------------------------------
# GitHub Auto-Backup: admin edit na tuah paoh ah database cu
# GitHub PRIVATE repo ah amah tein a fim; website a restart /
# deploy i database a lawng a si ahcun a thawk ah amah tein a
# lak kir. Env var GITHUB_BACKUP_TOKEN a um lo ahcun a kal lo.
# ------------------------------------------------------------------
import json as _gh_json
import threading as _gh_threading
import time as _gh_time
import urllib.error as _gh_urlerr
import urllib.request as _gh_urlreq

GH_BACKUP_REPO = os.environ.get("GITHUB_BACKUP_REPO",
                                "cungzahmung/rcbc-backup")
GH_BACKUP_PATH = "church_directory.db"
_gh_state = {"dirty": False, "since": 0.0, "last_result": ""}


def _gh_token():
    return os.environ.get("GITHUB_BACKUP_TOKEN", "").strip()


def _gh_api(method, path, payload=None, raw=False):
    req = _gh_urlreq.Request("https://api.github.com" + path,
                             method=method)
    req.add_header("Authorization", "Bearer " + _gh_token())
    req.add_header("Accept", "application/vnd.github.raw" if raw
                   else "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    data = None
    if payload is not None:
        data = _gh_json.dumps(payload).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    with _gh_urlreq.urlopen(req, data=data, timeout=30) as resp:
        body = resp.read()
    if raw:
        return body
    return _gh_json.loads(body.decode("utf-8")) if body else {}


def _gh_snapshot_bytes():
    tmp_path = DATABASE + ".ghtmp"
    if os.path.exists(tmp_path):
        os.remove(tmp_path)
    src = sqlite3.connect(DATABASE)
    dst = sqlite3.connect(tmp_path)
    src.backup(dst)
    dst.close()
    src.close()
    with open(tmp_path, "rb") as fh:
        data = fh.read()
    os.remove(tmp_path)
    return data


def _gh_repo_is_empty():
    try:
        _gh_api("GET", "/repos/" + GH_BACKUP_REPO + "/git/ref/heads/main")
        return False
    except _gh_urlerr.HTTPError as e:
        if e.code in (404, 409):
            return True
        raise


def _gh_seed_repo():
    """Repo lawng (commit hmasa bik a um lo) ahcun Git Data API nih 409 in
    a leh - Contents API in file pakhat chiah hmasa in commit hmasa bik
    ser a hau."""
    body = ("RCBC website auto-backup repository.\n"
            "church_directory.db = website data backup file.\n").encode()
    _gh_api("PUT", "/repos/" + GH_BACKUP_REPO + "/contents/backup-info.txt",
            {"message": "Initialize backup repo",
             "content": base64.b64encode(body).decode("ascii"),
             "branch": "main"})


def _gh_upload_backup():
    """Database snapshot kha GitHub repo ah commit tuah."""
    if _gh_repo_is_empty():
        _gh_seed_repo()
    data = _gh_snapshot_bytes()
    repo = "/repos/" + GH_BACKUP_REPO
    blob = _gh_api("POST", repo + "/git/blobs", {
        "content": base64.b64encode(data).decode("ascii"),
        "encoding": "base64",
    })
    head_sha = None
    tree_sha = None
    try:
        ref = _gh_api("GET", repo + "/git/ref/heads/main")
        head_sha = ref["object"]["sha"]
        commit = _gh_api("GET", repo + "/git/commits/" + head_sha)
        tree_sha = commit["tree"]["sha"]
    except _gh_urlerr.HTTPError as e:
        if e.code not in (404, 409):
            raise
    tree_payload = {"tree": [{"path": GH_BACKUP_PATH, "mode": "100644",
                              "type": "blob", "sha": blob["sha"]}]}
    if tree_sha:
        tree_payload["base_tree"] = tree_sha
    tree = _gh_api("POST", repo + "/git/trees", tree_payload)
    commit_payload = {"message": "Auto-backup " + date.today().isoformat(),
                      "tree": tree["sha"]}
    if head_sha:
        commit_payload["parents"] = [head_sha]
    new_commit = _gh_api("POST", repo + "/git/commits", commit_payload)
    if head_sha:
        _gh_api("PATCH", repo + "/git/refs/heads/main",
                {"sha": new_commit["sha"]})
    else:
        _gh_api("POST", repo + "/git/refs",
                {"ref": "refs/heads/main", "sha": new_commit["sha"]})
    try:
        db = sqlite3.connect(DATABASE)
        db.execute("INSERT OR REPLACE INTO settings (key, value) "
                   "VALUES ('gh_backup_at', ?)",
                   (date.today().isoformat(),))
        db.commit()
        db.close()
    except Exception:
        pass


def _gh_download_backup():
    repo = "/repos/" + GH_BACKUP_REPO
    return _gh_api("GET", repo + "/contents/" + GH_BACKUP_PATH, raw=True)


def _db_is_empty():
    try:
        db = sqlite3.connect(DATABASE)
        n = 0
        for tbl in ("members", "news", "events"):
            n += db.execute("SELECT COUNT(*) FROM " + tbl).fetchone()[0]
        db.close()
        return n == 0
    except Exception:
        return False


def _gh_restore_if_empty():
    """Data a um cang ahcun a tongh lo; a lawng lawng a si ahcun
    GitHub backup in a lak kir."""
    if not _gh_token():
        return
    try:
        if not _db_is_empty():
            return
        raw = _gh_download_backup()
        if raw[:16] != b"SQLite format 3\x00":
            return
        with open(DATABASE, "wb") as fh:
            fh.write(raw)
        init_db()
        print("GitHub auto-restore: backup in data lak kir a si.", flush=True)
    except Exception as e:
        print("GitHub auto-restore a tling lo:", e, flush=True)


def _gh_worker():
    while True:
        _gh_time.sleep(20)
        try:
            if (_gh_state["dirty"]
                    and _gh_time.time() - _gh_state["since"] > 30):
                _gh_state["dirty"] = False
                _gh_upload_backup()
                _gh_state["last_result"] = ("A tling - "
                                            + date.today().isoformat())
                print("GitHub auto-backup: a tling.", flush=True)
        except Exception as e:
            _gh_state["dirty"] = True
            _gh_state["since"] = _gh_time.time() + 600
            _gh_state["last_result"] = "A tling lo: " + str(e)
            print("GitHub auto-backup a tling lo:", e, flush=True)


def init_auto_backup():
    """Live site thawk ah hmet ding (Render copy lawng a hmet)."""
    if not _gh_token():
        return
    _gh_restore_if_empty()
    t = _gh_threading.Thread(target=_gh_worker, daemon=True)
    t.start()
    print("GitHub auto-backup worker a thawk cang.", flush=True)


@app.after_request
def _gh_mark_dirty(response):
    try:
        if (request.method == "POST" and _gh_token() and is_admin()
                and response.status_code < 400):
            _gh_state["dirty"] = True
            _gh_state["since"] = _gh_time.time()
    except Exception:
        pass
    return response


init_db()
init_auto_backup()


def get_news():
    """News vialte lak - ni thar bik hmasa (date desc, id desc)."""
    db = get_db()
    try:
        rows = db.execute(
            "SELECT * FROM news ORDER BY date DESC, id DESC"
        ).fetchall()
    except sqlite3.OperationalError:
        # Table a um rih lo ahcun (init_db run hlan) ser law lak
        init_db()
        rows = db.execute(
            "SELECT * FROM news ORDER BY date DESC, id DESC"
        ).fetchall()
    return rows



WEEKLY_SERVICES = {
    "friday": {"label": "Friday Zan Pumhnak", "time": "7:00 PM",
               "weekday": 4},
    "sunday": {"label": "Sunday Pumhnak", "time": "1:00 PM - 3:00 PM",
               "weekday": 6},
}


def next_service_date(weekday):
    """A ra lai mi cu ni cu (tuni a si ahcun tuni) date a kir."""
    today = date.today()
    return today + timedelta(days=(weekday - today.weekday()) % 7)


DEFAULT_SERVICE_TIMES = {
    "friday_time": "7:00 PM",
    "sunday_time": "1:00 PM - 3:00 PM",
}


def get_service_times():
    """Pumhnak caan pahnih lak (DB settings, um lo ah default)."""
    db = get_db()
    try:
        rows = db.execute("SELECT key, value FROM settings").fetchall()
    except sqlite3.OperationalError:
        init_db()
        rows = db.execute("SELECT key, value FROM settings").fetchall()
    vals = {r["key"]: (r["value"] or "") for r in rows}
    return {k: (vals.get(k) or d) for k, d in DEFAULT_SERVICE_TIMES.items()}


DUTY_ROLE_SUGGESTIONS = [
    "Pumh Hruaitu", "Hramthok Thlacam", "Pumhnak In",
    "Bible Rel", "Solo", "Duet", "Thawhlawm ca Thlacam",
    "Zapi Thlacam Hruaitu", "Sermon", "Thawngtha Chim",
    "Hlaremh", "Donghnak Hla", "Thluachuah Pek Nak",
    "Donghnak Thlacam", "Thawhlawm Kholhtu",
]


def get_scriptures():
    """Pathian bia vialte lak - ni thar bik hmasa."""
    db = get_db()
    try:
        rows = db.execute(
            "SELECT * FROM scriptures ORDER BY date DESC, id DESC"
        ).fetchall()
    except sqlite3.OperationalError:
        init_db()
        rows = db.execute(
            "SELECT * FROM scriptures ORDER BY date DESC, id DESC"
        ).fetchall()
    return rows


def get_services():
    """Caan ngeitu service vialte lak, an tlar (items) telh in.
    Ni thar bik hmasa; tlar cu sort_order ningin an i rem."""
    db = get_db()
    sql_s = "SELECT * FROM services ORDER BY service_date DESC, id DESC"
    sql_i = ("SELECT * FROM service_items WHERE service_id=? "
             "ORDER BY sort_order ASC, id ASC")
    try:
        srows = db.execute(sql_s).fetchall()
    except sqlite3.OperationalError:
        init_db()
        srows = db.execute(sql_s).fetchall()
    _times = get_service_times()
    out = []
    for r in srows:
        d = dict(r)
        _stype = d.get("service_type") or ""
        if _stype == "friday":
            d["service_time"] = _times["friday_time"]
        elif _stype == "sunday":
            d["service_time"] = _times["sunday_time"]
        else:
            d["service_time"] = ""
        d["items"] = [dict(x) for x in db.execute(sql_i, (r["id"],)).fetchall()]
        out.append(d)
    return out


def _service_form_items():
    """Form in a ra mi role/person tlar pawl lak (a lawng lo mi)."""
    roles = request.form.getlist("role")
    persons = request.form.getlist("person")
    items = []
    for i in range(max(len(roles), len(persons))):
        role = roles[i].strip() if i < len(roles) else ""
        person = persons[i].strip() if i < len(persons) else ""
        if role or person:
            items.append((role, person, len(items)))
    return items


def _save_service_items(db, service_id, items):
    db.execute("DELETE FROM service_items WHERE service_id=?", (service_id,))
    db.executemany(
        "INSERT INTO service_items (service_id, role, person, sort_order) "
        "VALUES (?,?,?,?)",
        [(service_id, role, person, order) for role, person, order in items],
    )


def _family_members_from_form():
    """Directory form in chungtel min vialte lak.
    Tlar pakhat cio (family_member) in a ra mi le, textarea
    (family_members - tlar pakhat ah min pakhat, comma zong
    a ngah) in a ra mi fonh; a lawng mi hloh, tlar khat ah
    min khat in a kir (newline in then)."""
    names = []
    for raw in request.form.getlist("family_member"):
        name = (raw or "").strip()
        if name:
            names.append(name)
    extra = request.form.get("family_members", "") or ""
    for part in extra.replace(",", "\n").splitlines():
        name = part.strip()
        if name:
            names.append(name)
    return "\n".join(names)


def _members_list(value):
    """Save mi family_members cafang kha min list ah thlen."""
    if not value:
        return []
    out = []
    for part in str(value).replace(",", "\n").splitlines():
        name = part.strip()
        if name:
            out.append(name)
    return out


def _member_dict(row):
    """sqlite Row kha dict ah thlen, members_list chap chih."""
    d = dict(row)
    if "family_members" not in d:
        d["family_members"] = ""
    d["members_list"] = _members_list(d.get("family_members"))
    return d


LEADER_POSITIONS = [
    "Pastor", "Associate Pastor", "Chairman", "Vice Chairman",
    "Secretary", "Assistant Secretary", "Treasurer",
    "Assistant Treasurer", "Deacon", "Elder", "Youth Leader",
    "Women Leader", "CE Leader", "Music Leader", "Member",
]

_LEADER_PHOTO_MAX = 8 * 1024 * 1024  # 8 MB


def _detect_image_mimetype(data):
    if data[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return ""


def _read_leader_photo(file_storage):
    """Upload mi photo lak. (data, mimetype, error) a kir:
    file um lo ah (None, '', ''); dik lo / ngan tuk ah
    (None, '', error); dik ah (bytes, mimetype, '')."""
    if file_storage is None or not getattr(file_storage, "filename", ""):
        return None, "", ""
    data = file_storage.read()
    if not data:
        return None, "", ""
    if len(data) > _LEADER_PHOTO_MAX:
        return None, "", "Photo cu 8 MB nak ngan deuh lo ding."
    detected = _detect_image_mimetype(data)
    allowed = {"image/jpeg", "image/png", "image/webp", "image/gif"}
    ext = os.path.splitext(file_storage.filename or "")[1].lower()
    ext_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg",
               ".png": "image/png", ".webp": "image/webp",
               ".gif": "image/gif"}
    claimed = (file_storage.mimetype or "").lower()
    if detected not in allowed:
        return None, "", "Photo cu JPG, PNG, WebP, GIF lawng a ngah."
    if ext in ext_map and ext_map[ext] != detected:
        return None, "", "Photo file phun a dik lo."
    if claimed and claimed not in allowed and claimed != "application/octet-stream":
        return None, "", "Photo cu JPG, PNG, WebP, GIF lawng a ngah."
    return data, detected, ""


def _leader_form_data():
    position = request.form.get("position", "").strip()
    if position == "Other":
        other = (request.form.get("position_other", "").strip()
                 or request.form.get("custom_position", "").strip()
                 or request.form.get("other_position", "").strip())
        if other:
            position = other
    try:
        sort_order = int(request.form.get("sort_order", "0") or 0)
    except (TypeError, ValueError):
        sort_order = 0
    return {
        "name": request.form.get("name", "").strip(),
        "position": position,
        "phone": request.form.get("phone", "").strip(),
        "email": request.form.get("email", "").strip(),
        "bio": request.form.get("bio", "").strip(),
        "sort_order": sort_order,
    }


def get_leaders():
    """Leader vialte lak: code LEADERS le website form in chiah
    mi (SQLite leaders table) fonh. DB mi cu sort_order, id
    ningin an i rem; code mi cu id=None, has_photo=False
    (Edit/Delete button a um lo). DB ah a rak lut cang mi
    (seed) code leader cu voi hnih an lang lo nak ding
    DB mi lawng kan lang ter."""
    db = get_db()
    try:
        rows = db.execute(
            "SELECT * FROM leaders ORDER BY sort_order ASC, id ASC"
        ).fetchall()
    except sqlite3.OperationalError:
        init_db()
        rows = db.execute(
            "SELECT * FROM leaders ORDER BY sort_order ASC, id ASC"
        ).fetchall()
    db_leaders = []
    seen = set()
    for r in rows:
        d = dict(r)
        photo = d.pop("photo_data", None)
        d.pop("photo_mimetype", None)
        d["has_photo"] = bool(photo)
        name = (d.get("name") or "").strip()
        d["initial"] = name[:1].upper() if name else "?"
        seen.add(((d.get("name") or "").strip().lower(),
                  (d.get("position") or "").strip().lower()))
        db_leaders.append(d)
    merged = []
    for p in LEADERS:
        name = (p.get("name") or "").strip()
        if not name:
            continue
        position = p.get("role", p.get("position", "")) or ""
        if (name.lower(), position.strip().lower()) in seen:
            continue
        merged.append({
            "id": None, "name": name, "position": position,
            "phone": p.get("phone", "") or "",
            "email": p.get("email", "") or "",
            "bio": p.get("bio", "") or "",
            "sort_order": p.get("sort_order", 0) or 0,
            "has_photo": False, "initial": name[:1].upper(),
        })
    merged.extend(db_leaders)
    return merged


EVENT_CATEGORIES = {
    "bupi": BUPI_EVENTS,
    "youth": YOUTH_EVENTS,
    "ce": CE_EVENTS,
    "mission": MISSION_EVENTS,
    "nubu": NUBU_EVENTS,
}


def get_events(category):
    """Category i event vialte lak: code dict (BUPI_EVENTS tbk) le
    website form in chiah mi (SQLite events table) fonh.
    {date: [event, ...]} ningin a kir; form in chiah mi lawng
    id an ngei (delete khawh nak)."""
    merged = {}
    for day, evs in EVENT_CATEGORIES.get(category, {}).items():
        for ev in evs:
            merged.setdefault(day, []).append({
                "id": None,
                "title": ev.get("title", ""),
                "time": ev.get("time", ""),
                "place": ev.get("place", ""),
                "note": ev.get("note", ""),
            })
    db = get_db()
    try:
        rows = db.execute(
            "SELECT * FROM events WHERE category=? ORDER BY date, id",
            (category,),
        ).fetchall()
    except sqlite3.OperationalError:
        init_db()
        rows = db.execute(
            "SELECT * FROM events WHERE category=? ORDER BY date, id",
            (category,),
        ).fetchall()
    for r in rows:
        merged.setdefault(r["date"], []).append({
            "id": r["id"],
            "title": r["title"],
            "time": r["time"],
            "place": r["place"],
            "note": r["note"],
        })
    return merged


# ------------------------------------------------------------------
# Calendar helper - thla calendar ser, event ni pawl mark
# ------------------------------------------------------------------
def build_calendar(year, month, events):
    cal = cal_module.Calendar(firstweekday=6)  # Sunday first
    weeks = cal.monthdayscalendar(year, month)
    month_name = cal_module.month_name[month]
    prev_y, prev_m = (year - 1, 12) if month == 1 else (year, month - 1)
    next_y, next_m = (year + 1, 1) if month == 12 else (year, month + 1)
    days = []
    for week in weeks:
        row = []
        for d in week:
            if d == 0:
                row.append(None)
            else:
                key = f"{year:04d}-{month:02d}-{d:02d}"
                row.append({"day": d, "key": key, "events": events.get(key, [])})
        days.append(row)
    return {
        "year": year, "month": month, "month_name": month_name,
        "weeks": days, "prev_y": prev_y, "prev_m": prev_m,
        "next_y": next_y, "next_m": next_m,
    }


def sorted_events(events):
    out = []
    for day in sorted(events.keys()):
        for ev in events[day]:
            out.append({"date": day, **ev})
    return out

# ------------------------------------------------------------------
# Base layout / CSS
# ------------------------------------------------------------------
BASE_HEAD = """
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<title>{{ title }} - Raleigh Chin Baptist Church</title>
<style>
*{box-sizing:border-box} html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
:root{--bg:#f9f6f0;--card:#ffffff;--text:#222222;--border:#e5ddd0;--tdborder:#e0d6c6;--th:#efe6d8;--nav:#2f2a26;--brand-text:#5b1f1f;--muted:#666666;--soft:#fdfaf3;--empty-bg:#faf7f1;--link:#7a2b2b;--ev:#fdf0c9;--ev-text:#333333}
body.dark{--bg:#13151b;--card:#1e212a;--text:#e9e6e0;--border:#343947;--tdborder:#343947;--th:#282d3a;--nav:#0c0e13;--brand-text:#e3acac;--muted:#a3a099;--soft:#232733;--empty-bg:#191c24;--link:#e3acac;--ev:#4a3f1c;--ev-text:#f2e3ae}
body{margin:0;font-family:Georgia,serif;color:var(--text);background:var(--bg);line-height:1.55;overflow-wrap:break-word}
main a{color:var(--link)}
.theme-btn{background:transparent;border:1px solid #c9a227;color:#fff;border-radius:20px;padding:8px 13px;min-height:44px;cursor:pointer;font-family:Arial,sans-serif;font-size:14px}
img{max-width:100%} a{touch-action:manipulation}
header{background:#5b1f1f;color:#fff;padding:28px 20px;text-align:center}
header h1{margin:0;font-size:clamp(22px,6vw,30px);line-height:1.2} header p{margin:6px 0 0;opacity:.9}
nav{background:var(--nav);display:flex;flex-wrap:wrap;justify-content:center;gap:4px;padding:10px}
nav a{color:#fff;text-decoration:none;padding:9px 14px;border-radius:20px;font-family:Arial,sans-serif;font-size:14px;min-height:44px;display:inline-flex;align-items:center}
nav a:hover,nav a.active{background:#c9a227;color:#111}
main{max-width:1000px;margin:0 auto;padding:28px 18px 50px;width:100%}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;margin:16px 0;overflow-wrap:break-word}
h2{color:var(--brand-text);font-size:clamp(20px,5vw,26px)} h3{color:var(--brand-text);margin-top:0}
.btn{background:#5b1f1f;color:#fff;border:0;padding:10px 18px;border-radius:8px;cursor:pointer;font-size:16px;min-height:44px}
.btn:hover{background:#7a2b2b} input,textarea,select{width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;margin:5px 0 12px;font-size:16px;min-height:44px;background:var(--card);color:var(--text)}
textarea{min-height:0} input[type=file]{min-height:0} input[type=checkbox]{min-height:0}
table{width:100%;border-collapse:collapse;background:var(--card)} th,td{border:1px solid var(--tdborder);padding:10px;text-align:left;vertical-align:top}
th{background:var(--th)} .cal{width:100%;border-collapse:collapse;background:var(--card)}
.cal th{background:#5b1f1f;color:#fff;text-align:center;padding:8px}
.cal td{width:14.28%;height:92px;border:1px solid #e0d6c6;vertical-align:top;padding:6px;font-size:13px}
.cal td.empty{background:var(--empty-bg)} .cal .ev{background:var(--ev);color:var(--ev-text);border-radius:6px;padding:3px 5px;margin-top:4px;font-size:12px}
.cal-nav{display:flex;justify-content:space-between;align-items:center;margin:14px 0}
.cal-nav a{color:var(--brand-text);font-weight:bold;text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.leader-card{text-align:center}
.leader-photo{width:150px;height:150px;object-fit:cover;border-radius:50%;display:block;margin:0 auto 12px}
.leader-placeholder{width:150px;height:150px;border-radius:50%;background:var(--th);color:var(--brand-text);display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:bold;margin:0 auto 12px;font-family:Georgia,serif}
.leader-actions{display:flex;gap:10px;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:10px}
.auto-expand{overflow:hidden;min-height:180px;line-height:1.65}
.motto{font-style:italic;color:var(--brand-text);font-size:18px;border-left:4px solid #c9a227;background:var(--soft);padding:10px 14px;border-radius:8px;margin:10px 0}
.scripture-body{white-space:pre-line;font-size:18px;line-height:1.75;background:var(--soft);border-left:4px solid #c9a227;padding:16px 18px;border-radius:8px;margin-top:10px}
.duty-table td:first-child{font-weight:bold;width:46%;color:var(--brand-text)}
.duty-head{border-bottom:2px solid #5b1f1f;padding-bottom:8px;margin-bottom:6px}
.duty-rows{display:flex;flex-direction:column;gap:8px;margin:8px 0 12px}
.duty-row{display:flex;gap:8px;align-items:flex-start}
.duty-row input{margin:0;flex:1;min-width:0}
.family-rows{display:flex;flex-direction:column;gap:8px;margin:8px 0 12px}
.family-row{display:flex;gap:8px;align-items:flex-start}
.family-row input{margin:0;flex:1;min-width:0}
.family-row .fam-no{font-family:Arial,sans-serif;font-size:13px;color:var(--brand-text);padding-top:12px;min-width:22px;text-align:right}
.member-list{margin:0;padding-left:18px;white-space:normal;line-height:1.5}
.member-count{color:#666;font-size:13px;font-family:Arial,sans-serif}
details.edit-box{margin-top:14px;text-align:left} details.edit-box summary{cursor:pointer;color:var(--brand-text);font-weight:bold}
footer{background:#2f2a26;color:#ddd;text-align:center;padding:22px 16px;font-size:14px;overflow-wrap:anywhere}
{% if has_logo %}body::before{content:"";position:fixed;inset:0;background:url("/church-logo") center center / min(74vmin,600px) no-repeat;opacity:.07;pointer-events:none;z-index:0}
header,nav,main,footer{position:relative;z-index:1}{% endif %}
.empty{color:var(--muted);font-style:italic} .search{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-start}
.search input{flex:1;min-width:200px} label{font-family:Arial,sans-serif;font-size:14px;font-weight:bold}
button{min-height:40px;padding:8px 14px;cursor:pointer}
/* --- Mobile / Phone (responsive) --- */
@media (max-width:700px){
 header{padding:20px 14px} nav{padding:8px 6px;gap:6px}
 nav a{padding:8px 11px;font-size:13px}
 main{padding:18px 10px 36px} .card{padding:14px 12px;margin:12px 0;border-radius:10px}
 .grid{grid-template-columns:1fr;gap:12px}
 table:not(.cal){display:block;overflow-x:auto;-webkit-overflow-scrolling:touch;white-space:nowrap;max-width:100%}
 th,td{padding:8px}
 .cal{table-layout:fixed} .cal th{padding:6px 1px;font-size:11px}
 .cal td{height:56px;padding:3px;font-size:11px;overflow:hidden}
 .cal .ev{font-size:10px;line-height:1.25;padding:2px 3px;margin-top:2px;overflow-wrap:anywhere}
 .cal-nav{flex-wrap:wrap;gap:8px} .cal-nav a{min-height:44px;display:inline-flex;align-items:center}
 .cal-nav span{font-size:14px;text-align:center}
 .search{flex-direction:column} .search input{min-width:0;width:100%}
 .search .btn{width:100%} form .btn{width:100%}
 .leader-photo{width:120px;height:120px} .leader-placeholder{width:120px;height:120px;font-size:42px}
 .leader-actions{gap:8px} details.edit-box summary{padding:8px 0}
 footer{font-size:13px}
}
@media (max-width:380px){
 .cal td{height:48px;font-size:10px} .cal .ev{font-size:9px}
 nav a{padding:8px 9px;font-size:12px}
}
@media (max-width:700px){
 .scripture-body{font-size:16px;padding:12px}
 .duty-row{flex-direction:column}
 .duty-row input,.duty-row button{width:100%}
 .duty-table td:first-child{width:44%}
 .family-row{flex-direction:column}
 .family-row input,.family-row button{width:100%}
 .family-row .fam-no{padding-top:0;text-align:left}
 table .member-list{white-space:normal}
}
/* ===== DESIGN THAR (Chin Bethel bantuk dawh deuh nak) ===== */
body{font-family:'Outfit',Arial,sans-serif}
h1,h2,h3,header .church-name,.hero-name,.cd .num{font-family:'Montserrat',Georgia,serif}
header{background:linear-gradient(135deg,#732a2a 0%,#5d3256 55%,#343453 100%);border-bottom:3px solid #c9a227;padding:30px 16px 24px}
header .church-name{letter-spacing:.5px;text-shadow:0 2px 10px rgba(0,0,0,.35)}
.marquee{overflow:hidden;white-space:nowrap;margin-top:8px}
.marquee-in{display:inline-block;white-space:nowrap;padding-left:100%;animation:mqfly 16s linear infinite;font-size:clamp(15px,3.4vw,19px);color:#ffe9a8;font-weight:500}
@keyframes mqfly{0%{transform:translateX(0)}100%{transform:translateX(-100%)}}
@media (prefers-reduced-motion: reduce){.marquee-in{animation:none;padding-left:0}}
nav{position:sticky;top:0;z-index:60;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.card{border-radius:16px;box-shadow:0 8px 26px rgba(30,20,10,.10);animation:fadeUp .5s ease both}
h2{position:relative;padding-bottom:8px}
h2::after{content:"";position:absolute;left:0;bottom:0;width:56px;height:3px;border-radius:2px;background:#c9a227}
.btn,.btn-danger{border-radius:24px;box-shadow:0 4px 12px rgba(91,31,31,.28);transition:transform .15s ease,box-shadow .15s ease}
.btn:hover{transform:translateY(-1px);box-shadow:0 8px 18px rgba(91,31,31,.32)}
footer{border-top:3px solid #c9a227}
.leader-photo{border:3px solid #c9a227;box-shadow:0 6px 18px rgba(0,0,0,.18)}
.leader-placeholder{border:3px solid #c9a227}
input:focus,textarea:focus,select:focus{outline:none;border-color:#c9a227;box-shadow:0 0 0 3px rgba(201,162,39,.25)}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.hero{background:linear-gradient(160deg,#773030 0%,#5f3556 55%,#3a3a5b 100%);color:#fff;border-radius:16px;padding:38px 22px 30px;text-align:center;margin:16px 0;box-shadow:0 12px 32px rgba(20,10,20,.28);animation:fadeUp .5s ease both;position:relative;z-index:1}
.hero-logo{width:112px;height:112px;border-radius:50%;background:#fff;padding:5px;box-shadow:0 8px 22px rgba(0,0,0,.35);margin-bottom:12px}
.hero-name{font-size:clamp(26px,6vw,40px);font-weight:800;letter-spacing:.5px;line-height:1.2}
.hero-verse{font-size:clamp(18px,4.4vw,25px);font-style:italic;margin:14px auto 2px;max-width:640px;line-height:1.45}
.hero-ref{color:#ffe9a8;margin:0 0 14px;font-size:15px;letter-spacing:1px}
.hero-chips{margin:10px 0 4px}
.slideshow{position:relative;border-radius:16px;overflow:hidden;margin:16px 0;box-shadow:0 12px 32px rgba(20,10,20,.25);background:#222;aspect-ratio:16/9}
.slideshow .slide{position:absolute;inset:0;opacity:0;transition:opacity .8s ease}
.slideshow .slide.on{opacity:1;z-index:1}
.slideshow .slide img{width:100%;height:100%;object-fit:cover;display:block}
.slide-cap{position:absolute;left:0;right:0;bottom:0;padding:26px 76px 12px 16px;color:#fff;font-size:15px;background:linear-gradient(transparent,rgba(0,0,0,.65))}
.slide-dots{position:absolute;right:12px;bottom:12px;display:flex;gap:6px;z-index:2}
.slide-dots button{width:9px;height:9px;border-radius:50%;border:0;background:rgba(255,255,255,.45);padding:0;cursor:pointer}
.slide-dots button.on{background:#ffe9a8}
@media (max-width:640px){.slideshow{aspect-ratio:4/3}.slide-cap{font-size:13px}}
@media (prefers-reduced-motion:reduce){.slideshow .slide{transition:none}}
.social-btns{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}
.social-btn{display:inline-block;padding:10px 22px;border-radius:999px;color:#fff;font-weight:700;text-decoration:none}
.social-btn.fb{background:#1877f2}
.social-btn.ig{background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)}
.ok-note{background:#e7f6e7;border:1px solid #9ccc9c;border-radius:8px;padding:10px 12px}
.err-note{background:#fdeaea;border:1px solid #e5a3a3;border-radius:8px;padding:10px 12px}
.chip{display:inline-block;border:1px solid #c9a227;color:#ffe9a8;border-radius:20px;padding:6px 14px;margin:4px;font-size:14px;background:rgba(255,255,255,.06)}
.cd-title{margin-top:18px;font-size:15px;color:#ffe9a8;letter-spacing:.4px}
.cd{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:10px}
.cd .box{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.28);border-radius:12px;padding:10px 8px;min-width:76px}
.cd .num{font-size:27px;font-weight:800;line-height:1}
.cd .lab{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#ffe9a8;margin-top:4px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.g-item{margin:0}
.g-item img{width:100%;height:150px;object-fit:cover;border-radius:10px;display:block;box-shadow:0 4px 12px rgba(0,0,0,.15)}
.g-item figcaption{font-size:13px;margin-top:5px;color:var(--muted)}
.video-wrap{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;background:#000}
.video-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.video-box{margin:18px 0}
.yt-btn{background:#c4302b;box-shadow:0 4px 12px rgba(196,48,43,.30)}
.footer-edit-wrap{background:#1c1a17;padding:0 14px 16px}
.footer-edit{max-width:560px;margin:0 auto;text-align:left;background:rgba(255,255,255,.06);border-radius:10px;padding:6px 14px 12px}
.footer-edit summary{color:#ffe9a8}
</style></head><body>
<script>try{if(localStorage.getItem('rcbc-theme')==='dark'){document.body.classList.add('dark');}}catch(e){}</script>
<header><h1>Raleigh Chin Baptist Church</h1><div class="marquee"><span class="marquee-in">{{ church.tagline }}</span></div></header>
<nav>
<a href="/" class="{{ 'active' if active=='home' }}">Home</a>
{% if is_admin %}<a href="/directory" class="{{ 'active' if active=='directory' }}">Directory</a>{% endif %}
<a href="/church-event" class="{{ 'active' if active in ['church-event','bupi','youth','ce','mission','nubu'] }}">Church Event</a>
<a href="/church-leaders" class="{{ 'active' if active=='leaders' }}">Church Leaders</a>
<a href="/church-news" class="{{ 'active' if active=='news' }}">Church News</a>
<a href="/about" class="{{ 'active' if active=='about' }}">About Us</a>
<a href="/pathian-bia" class="{{ 'active' if active=='scripture' }}">Pathian Bia</a>
<a href="/caan-ngeitu" class="{{ 'active' if active=='caan' }}">Caan Ngeitu</a>
{% if is_admin %}<a href="/logout">Logout (Admin)</a>{% endif %}
{% if is_super %}<a href="/admin-users" class="{{ 'active' if active=='users' }}">Admin Users</a>{% endif %}
<button type="button" id="themeToggle" class="theme-btn" aria-label="Day / Night mode">&#127769; Night</button>
</nav>{% if is_admin %}<div style="background:#fdf0c9;color:#5b1f1f;text-align:center;padding:9px;font-family:Arial,sans-serif;font-size:14px">Admin in na lut cang{% if admin_label %} - <strong>{{ admin_label }}</strong>{% endif %} - edit tuah khawh a si. {% if not is_super %}<a href="/change-password">Password Thlen</a> &middot; {% endif %}<a href="/backup">Backup</a> &middot; <a href="/logout">Logout</a></div>{% endif %}<main>
"""
BASE_FOOT = """
</main><footer>Raleigh Chin Baptist Church
{% if church.address %} &middot; {{ church.address }}{% endif %}
{% if church.phone %} &middot; {{ church.phone }}{% endif %}
{% if church.email %} &middot; {{ church.email }}{% endif %}<br>
{{ footer_text }}{% if not is_admin %}<span style="float:right"><a href="/login" style="color:#ffe9a8">Admin Login</a></span>{% endif %}</footer>
{% if is_admin %}<div class="footer-edit-wrap"><details class="edit-box footer-edit"><summary>Footer Copyright Edit</summary>
<form method="post" action="/footer-text">
<label>Copyright cafang / Copyright text</label>
<input name="footer_text" value="{{ footer_text }}">
<button class="btn" type="submit">Save</button></form></details></div>{% endif %}
<script>
function autoExpandTA(el){el.style.height='auto';el.style.height=(el.scrollHeight+4)+'px';}
document.addEventListener('DOMContentLoaded',function(){
 var tb=document.getElementById('themeToggle');
 function themeLabel(){ if(tb){ tb.innerHTML=document.body.classList.contains('dark')?'&#9728;&#65038; Day':'&#127769; Night'; } }
 themeLabel();
 if(tb){ tb.addEventListener('click',function(){ document.body.classList.toggle('dark');
  try{ localStorage.setItem('rcbc-theme',document.body.classList.contains('dark')?'dark':'light'); }catch(e){}
  themeLabel(); }); }
 document.querySelectorAll('textarea.auto-expand').forEach(function(el){
  autoExpandTA(el); el.addEventListener('input',function(){autoExpandTA(el);});});
 document.addEventListener('click',function(e){
  if(e.target.classList.contains('add-duty-row')){
   var form=e.target.closest('form'); if(!form)return;
   var box=form.querySelector('.duty-rows'); if(!box)return;
   var row=box.querySelector('.duty-row'); if(!row)return;
   var clone=row.cloneNode(true);
   clone.querySelectorAll('input').forEach(function(i){i.value='';});
   box.appendChild(clone);
   var f=clone.querySelector('input'); if(f)f.focus();}
  if(e.target.classList.contains('remove-duty-row')){
   var r=e.target.closest('.duty-row'); var b=e.target.closest('.duty-rows');
   if(r&&b){ if(b.querySelectorAll('.duty-row').length>1){r.remove();}
    else{r.querySelectorAll('input').forEach(function(i){i.value='';});}}}
  if(e.target.classList.contains('add-family-row')){
   var fform=e.target.closest('form'); if(!fform)return;
   var fbox=fform.querySelector('.family-rows'); if(!fbox)return;
   var frow=fbox.querySelector('.family-row'); if(!frow)return;
   var fclone=frow.cloneNode(true);
   fclone.querySelectorAll('input').forEach(function(i){i.value='';});
   var fno=fclone.querySelector('.fam-no'); if(fno){fno.textContent=(fbox.querySelectorAll('.family-row').length+1)+'.';}
   fbox.appendChild(fclone);
   var ff=fclone.querySelector('input'); if(ff)ff.focus();}
  if(e.target.classList.contains('remove-family-row')){
   var fr=e.target.closest('.family-row'); var fb=e.target.closest('.family-rows');
   if(fr&&fb){ if(fb.querySelectorAll('.family-row').length>1){fr.remove();
     fb.querySelectorAll('.family-row').forEach(function(rw,ix){var n=rw.querySelector('.fam-no'); if(n)n.textContent=(ix+1)+'.';});}
    else{fr.querySelectorAll('input').forEach(function(i){i.value='';});}}}
 });
});
</script>
</body></html>
"""

CALENDAR_HTML = """
<div class="card"><h3>{{ cal.month_name }} {{ cal.year }}</h3>
<div class="cal-nav"><a href="?year={{cal.prev_y}}&month={{cal.prev_m}}">&larr; Previous</a>
<span>{{ cal.month_name }} {{ cal.year }}</span>
<a href="?year={{cal.next_y}}&month={{cal.next_m}}">Next &rarr;</a></div>
<table class="cal"><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>
{% for week in cal.weeks %}<tr>{% for d in week %}
{% if d is none %}<td class="empty"></td>{% else %}<td><strong>{{ d.day }}</strong>
{% for ev in d.events %}<div class="ev">{{ ev.title }}{% if ev.time %}<br>{{ ev.time }}{% endif %}{% if ev.note %}<br><em>{{ ev.note }}</em>{% endif %}</div>{% endfor %}</td>{% endif %}
{% endfor %}</tr>{% endfor %}</table></div>
<div class="card"><h3>Tuthla a Biapi mi Ni / This Month's Important Days - {{ cal.month_name }} {{ cal.year }}</h3>
{% if month_events %}<table><tr><th>Ni / Date</th><th>Event</th><th>Caan / Time</th><th>Hmun / Place</th><th>Note</th><th></th></tr>
{% for ev in month_events %}<tr><td>{{ ev.date }}</td><td>{{ ev.title }}</td><td>{{ ev.time }}</td><td>{{ ev.place }}</td><td>{{ ev.note }}</td>
<td>{% if is_admin and ev.id %}<form method="post" action="/events/delete/{{ ev.id }}" onsubmit="return confirm('Hi event hi delete duh taktak maw?')"><input type="hidden" name="next" value="{{ request_path }}?year={{ cal.year }}&amp;month={{ cal.month }}"><button type="submit">Delete</button></form>{% endif %}</td></tr>{% endfor %}</table>
{% else %}<p class="empty">Tuthla ({{ cal.month_name }}) ah event a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p>{% endif %}</div>
{% if is_admin %}<div class="card"><h3>Event Thar Chiah / Add Event</h3>
<p class="empty"> Date thim law, Title le Note tial;
"Add Event" hmet cun na thim mi ni kha calendar ah mark a si cang lai,
cun a cunglei table ah a lang cang lai.</p>
<form method="post" action="{{ request_path }}">
<label>Date / Ni *</label>
<input name="date" type="date" value="{{ today }}" required>
<label>Title / Event Lu *</label>
<input name="title" required placeholder="e.g. Bupi Pumh / Youth Service">
<label>Time / Caan</label>
<input name="time" placeholder="e.g. 1:00 PM">
<label>Place / Hmun</label>
<input name="place" placeholder="e.g. Church Hall">
<label>Note</label>
<textarea name="note" rows="3" placeholder="Theihternak / note tial..."></textarea>
<button class="btn" type="submit">Add Event / Event Chiah</button>
</form></div>{% endif %}
<div class="card"><h3>Event List - Vialte</h3>
{% if event_list %}{% for ev in event_list %}<p><strong>{{ ev.date }}</strong> - {{ ev.title }}
{% if ev.time %} &middot; {{ ev.time }}{% endif %}{% if ev.place %} &middot; {{ ev.place }}{% endif %}
{% if ev.note %}<br>{{ ev.note }}{% endif %}</p>{% endfor %}
{% else %}<p class="empty">Event a um rih lo.</p>{% endif %}</div>
"""


LOGIN_HTML = """
<h2>Admin Login / Admin Lut</h2>
<div class="card"><p>Hi website hi <strong>Admin lawngin</strong> edit khawh a si.
Public cu page vialte an zoh khawh, asinain zeihmanh an thlen / delete khawh lo.</p>
{% if error %}<p style="color:#b00020"><strong>{{ error }}</strong></p>{% endif %}
{% if msg %}<p style="color:#2e7d32"><strong>{{ msg }}</strong></p>{% endif %}
<form method="post">
<label>Username</label>
<input name="username" required autocomplete="username" placeholder="admin">
<label>Password</label>
<input name="password" type="password" required autocomplete="current-password">
<button class="btn" type="submit">Login / Lut</button>
</form>
<p class="empty">Admin na si lo ahcun kir than law page kha zoh lawng.</p>
<p>Admin account na ngei rih lo ahcun: <a href="/register">Admin Register / Account Ser &rarr;</a>
(Registration Code cu Super Admin sinah hal.)</p></div>
"""


REGISTER_HTML = """
<h2>Admin Register / Admin Account Ser</h2>
<div class="card"><p>Admin account thar ser nak. Na <strong>Rian (role)</strong> thim law,
na duh mi <strong>Username</strong> le <strong>Password</strong> kha nangmah tein ser -
Super Admin nih a set piak lo. <strong>Registration Code</strong> cu Super Admin
sinah hal (mi dang nih account an ser sual lo nak ding).</p>
{% if error %}<p style="color:#b00020"><strong>{{ error }}</strong></p>{% endif %}
{% if free_roles %}<form method="post">
<label>Rian / Role *</label>
<select name="role" required>{% for r in free_roles %}<option value="{{ r }}">{{ r }}</option>{% endfor %}</select>
<label>Username * (na duh mi)</label>
<input name="username" required autocomplete="username" placeholder="e.g. pastor.runlian">
<label>Password * (cafangkhat 6 nak tlawm lo)</label>
<input name="password" type="password" required autocomplete="new-password">
<label>Password Than Tial / Confirm Password *</label>
<input name="password2" type="password" required autocomplete="new-password">
<label>Registration Code * (Super Admin sinah hal)</label>
<input name="code" required placeholder="Code tial...">
<button class="btn" type="submit">Register / Account Ser</button>
</form>{% else %}<p class="empty">Admin rian 5 vialte account an ngei cang - account thar ser khawh a si lo.
Super Admin nih account pakhat a delete ahcun ser than khawh a si lai.</p>{% endif %}
<p class="empty">Account na ngei cang ahcun: <a href="/login">Admin Login &rarr;</a></p></div>
"""

USERS_HTML = """
<h2>Admin Users / Admin Hna</h2>
<div class="card"><h3>Super Admin</h3>
<p><strong>admin</strong> - Super Admin (hi account hi delete khawh a si lo;
password cu code / Render Environment ah a um).</p></div>
<div class="card"><h3>Admin Users ({{ users|length }} / 5)</h3>
{% if users %}<table><tr><th>Username</th><th>Rian / Role</th><th>Ser Ni / Created</th><th></th></tr>
{% for u in users %}<tr><td>{{ u.username }}</td><td>{{ u.role }}</td><td>{{ u.created }}</td>
<td><form method="post" action="/admin-users/delete/{{ u.id }}" onsubmit="return confirm('Hi account hi delete duh taktak maw?')"><button type="submit">Delete</button></form></td></tr>{% endfor %}</table>
{% else %}<p class="empty">Admin user account a um rih lo. Mi 5 hna nih /register in an account an ser lai.</p>{% endif %}</div>
<div class="card"><h3>Registration Code</h3>
<p>Account ser nak code atu: <strong>{{ reg_code }}</strong><br>
Hi code hi admin ding mi 5 hna lawng chimh hna - mi dang theihter hna hlah.</p>
<form method="post" action="/admin-users/code">
<label>Code Thar</label>
<input name="code" required placeholder="e.g. RCBC2026">
<button class="btn" type="submit">Code Thlen / Change Code</button>
</form></div>
<div class="card"><p class="empty">Rian a lawng mi: {% if free_roles %}{{ free_roles|join(', ') }}{% else %}a um lo (5 an kim cang){% endif %}.
Register page: <a href="/register">/register</a></p></div>
"""

CHANGE_PW_HTML = """
<h2>Password Thlen / Change Password</h2>
<div class="card">
{% if error %}<p style="color:#b00020"><strong>{{ error }}</strong></p>{% endif %}
{% if msg %}<p style="color:#2e7d32"><strong>{{ msg }}</strong></p>{% endif %}
<form method="post">
<label>Password Atu Mi / Current Password *</label>
<input name="current" type="password" required autocomplete="current-password">
<label>Password Thar / New Password * (cafangkhat 6 nak tlawm lo)</label>
<input name="new" type="password" required autocomplete="new-password">
<label>Password Thar Than Tial / Confirm New Password *</label>
<input name="new2" type="password" required autocomplete="new-password">
<button class="btn" type="submit">Password Thlen</button>
</form></div>
"""


# ------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if is_admin():
        return redirect(_safe_next(request.args.get("next", "")))
    error = ""
    msg = ""
    if request.args.get("registered"):
        msg = "Account ser a ngah cang! Atu login tuah khawh a si."
    if request.method == "POST":
        uname = request.form.get("username", "")
        pword = request.form.get("password", "")
        user_ok = hmac.compare_digest(uname, ADMIN_USERNAME)
        pass_ok = hmac.compare_digest(pword, ADMIN_PASSWORD)
        if user_ok and pass_ok:
            session.permanent = True
            session["admin_logged_in"] = True
            session["admin_super"] = True
            session["admin_label"] = "Super Admin"
            session.pop("admin_user_id", None)
            return redirect(_safe_next(request.form.get("next", "")
                                       or request.args.get("next", "")))
        # Admin user (DB) in login zuam
        try:
            db = get_db()
            row = db.execute(
                "SELECT * FROM admin_users WHERE LOWER(username)=LOWER(?)",
                (uname,)).fetchone()
        except Exception:
            init_db()
            row = get_db().execute(
                "SELECT * FROM admin_users WHERE LOWER(username)=LOWER(?)",
                (uname,)).fetchone()
        if row is not None and _check_password(pword, row["password_hash"]):
            session.permanent = True
            session["admin_logged_in"] = True
            session["admin_super"] = False
            session["admin_user_id"] = row["id"]
            session["admin_label"] = row["role"] or row["username"]
            return redirect(_safe_next(request.form.get("next", "")
                                       or request.args.get("next", "")))
        error = "Username asilole Password a dik lo. Than rak zuam."
    html = BASE_HEAD + LOGIN_HTML + BASE_FOOT
    return render_template_string(
        html, title="Admin Login", active="login", church=CHURCH,
        error=error, msg=msg)


@app.route("/logout")
def logout():
    for key in ("admin_logged_in", "admin_super", "admin_user_id",
                "admin_label"):
        session.pop(key, None)
    return redirect(url_for("home"))


def super_required(view):
    """Super Admin lawng: admin user a si ahcun home ah kuat."""

    @wraps(view)
    def wrapped(*args, **kwargs):
        if not is_admin():
            return redirect(url_for("login", next=request.path))
        if not is_super_admin():
            return redirect(url_for("home"))
        return view(*args, **kwargs)

    return wrapped


def get_admin_users():
    """Admin user vialte lak (role ningin an i rem)."""
    db = get_db()
    try:
        rows = db.execute("SELECT * FROM admin_users ORDER BY id").fetchall()
    except Exception:
        init_db()
        rows = db.execute("SELECT * FROM admin_users ORDER BY id").fetchall()
    return [dict(r) for r in rows]


def get_register_code():
    """Registration code lak (settings, um lo ah default)."""
    try:
        db = get_db()
        row = db.execute(
            "SELECT value FROM settings WHERE key='register_code'"
        ).fetchone()
        return (row["value"] if row and row["value"]
                else DEFAULT_REGISTER_CODE)
    except Exception:
        return DEFAULT_REGISTER_CODE


@app.route("/register", methods=["GET", "POST"])
def register():
    users = get_admin_users()
    taken = {(u["role"] or "").strip().lower() for u in users}
    free_roles = [r for r in ADMIN_ROLES if r.lower() not in taken]
    error = ""
    if request.method == "POST":
        role = request.form.get("role", "").strip()
        uname = request.form.get("username", "").strip()
        pw1 = request.form.get("password", "")
        pw2 = request.form.get("password2", "")
        code = request.form.get("code", "")
        if not hmac.compare_digest(code, get_register_code()):
            error = "Registration Code a dik lo. Super Admin sinah hal than."
        elif role not in ADMIN_ROLES or role.lower() in taken:
            error = "Hi rian hi account a ngei cang / a dik lo. A dang thim."
        elif len(uname) < 3:
            error = "Username cu cafangkhat 3 nak tlawm lo ding."
        elif uname.lower() == ADMIN_USERNAME.lower():
            error = "Hi username hi Super Admin ta a si - a dang thim."
        elif any((u["username"] or "").lower() == uname.lower()
                 for u in users):
            error = "Hi username hi a um cang - a dang thim."
        elif len(pw1) < 6:
            error = "Password cu cafangkhat 6 nak tlawm lo ding."
        elif pw1 != pw2:
            error = "Password pahnih an i khat lo. Than tial."
        else:
            db = get_db()
            db.execute(
                "INSERT INTO admin_users (username, password_hash, role, "
                "created) VALUES (?,?,?,?)",
                (uname, _hash_password(pw1), role,
                 date.today().isoformat()))
            db.commit()
            return redirect(url_for("login", registered=1))
        users = get_admin_users()
        taken = {(u["role"] or "").strip().lower() for u in users}
        free_roles = [r for r in ADMIN_ROLES if r.lower() not in taken]
    html = BASE_HEAD + REGISTER_HTML + BASE_FOOT
    return render_template_string(
        html, title="Admin Register", active="register", church=CHURCH,
        free_roles=free_roles, error=error)


@app.route("/admin-users")
@super_required
def admin_users_page():
    users = get_admin_users()
    taken = {(u["role"] or "").strip().lower() for u in users}
    free_roles = [r for r in ADMIN_ROLES if r.lower() not in taken]
    html = BASE_HEAD + USERS_HTML + BASE_FOOT
    return render_template_string(
        html, title="Admin Users", active="users", church=CHURCH,
        users=users, free_roles=free_roles, reg_code=get_register_code())


@app.route("/admin-users/delete/<int:user_id>", methods=["POST"])
@super_required
def delete_admin_user(user_id):
    db = get_db()
    db.execute("DELETE FROM admin_users WHERE id=?", (user_id,))
    db.commit()
    return redirect(url_for("admin_users_page"))


@app.route("/admin-users/code", methods=["POST"])
@super_required
def change_register_code():
    code = request.form.get("code", "").strip()
    if code:
        db = get_db()
        sql = "INSERT OR REPLACE INTO settings (key, value) VALUES (?,?)"
        try:
            db.execute(sql, ("register_code", code))
            db.commit()
        except sqlite3.OperationalError:
            init_db()
            db.execute(sql, ("register_code", code))
            db.commit()
    return redirect(url_for("admin_users_page"))


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if is_super_admin():
        return redirect(url_for("admin_users_page"))
    error = msg = ""
    if request.method == "POST":
        db = get_db()
        row = db.execute("SELECT * FROM admin_users WHERE id=?",
                         (session.get("admin_user_id"),)).fetchone()
        cur = request.form.get("current", "")
        new = request.form.get("new", "")
        new2 = request.form.get("new2", "")
        if row is None:
            return redirect(url_for("logout"))
        if not _check_password(cur, row["password_hash"]):
            error = "Password atu mi a dik lo."
        elif len(new) < 6:
            error = "Password thar cu cafangkhat 6 nak tlawm lo ding."
        elif new != new2:
            error = "Password thar pahnih an i khat lo. Than tial."
        else:
            db.execute("UPDATE admin_users SET password_hash=? WHERE id=?",
                       (_hash_password(new), row["id"]))
            db.commit()
            msg = "Password thlen a ngah cang."
    html = BASE_HEAD + CHANGE_PW_HTML + BASE_FOOT
    return render_template_string(
        html, title="Change Password", active="", church=CHURCH,
        error=error, msg=msg)


@app.route("/")
def home():
    html = BASE_HEAD + """
<div class="hero">
{% if has_logo %}<img class="hero-logo" src="/church-logo" alt="Church logo">{% endif %}
<div class="hero-name">{{ church.name }}</div>
{% if church.motto %}<p class="hero-verse">&ldquo;{{ church.motto }}&rdquo;</p>
<p class="hero-ref">&mdash; {{ church.motto_ref }}</p>{% endif %}
<div class="hero-chips"><span class="chip">Friday &middot; {{ times.friday_time }}</span><span class="chip">Sunday &middot; {{ times.sunday_time }}</span></div>
<div class="cd-title">A Ra Lai Mi Pumhnak &middot; Next Service: <b id="cdLabel"></b></div>
<div class="cd" id="cdBox">
<div class="box"><div class="num" id="cdD">0</div><div class="lab">Ni / Days</div></div>
<div class="box"><div class="num" id="cdH">0</div><div class="lab">Suimilam / Hrs</div></div>
<div class="box"><div class="num" id="cdM">0</div><div class="lab">Minute</div></div>
<div class="box"><div class="num" id="cdS">0</div><div class="lab">Second</div></div>
</div>
</div>
<script>
(function(){
 function pt(s){ var m=String(s).match(/(\\d{1,2})(?::(\\d{2}))?\\s*(AM|PM)/i); if(!m) return null;
  var h=parseInt(m[1],10)%12; if(/pm/i.test(m[3])) h+=12; return [h, parseInt(m[2]||'0',10)]; }
 function nxt(day, s){ var tm=pt(s); if(!tm) return null; var now=new Date(); var d=new Date(now);
  d.setDate(d.getDate()+((day-now.getDay()+7)%7)); d.setHours(tm[0],tm[1],0,0);
  if(d<=now) d.setDate(d.getDate()+7); return d; }
 var F=nxt(5, "{{ times.friday_time }}"), S=nxt(0, "{{ times.sunday_time }}");
 var tgt, lab;
 if(F && (!S || F<S)){ tgt=F; lab="Friday Zan Service"; } else if(S){ tgt=S; lab="Sunday Service"; }
 if(!tgt){ var b=document.getElementById('cdBox'); if(b) b.style.display='none'; return; }
 document.getElementById('cdLabel').textContent=lab;
 function tick(){ var diff=tgt-new Date(); if(diff<0) diff=0;
  var dd=Math.floor(diff/86400000), hh=Math.floor(diff/3600000)%24, mm=Math.floor(diff/60000)%60, ss=Math.floor(diff/1000)%60;
  document.getElementById('cdD').textContent=dd; document.getElementById('cdH').textContent=hh;
  document.getElementById('cdM').textContent=mm; document.getElementById('cdS').textContent=ss; }
 tick(); setInterval(tick,1000);
})();
</script>
{% if photos %}
<div class="slideshow" id="rcbcSlides">
{% for p in photos %}<div class="slide{% if loop.first %} on{% endif %}"><img src="/gallery-photo/{{ p.id }}" alt="{{ p.caption or 'Church activity photo' }}"{% if not loop.first %} loading="lazy"{% endif %}>{% if p.caption %}<div class="slide-cap">{{ p.caption }}</div>{% endif %}</div>
{% endfor %}{% if photos|length > 1 %}<div class="slide-dots">{% for p in photos %}<button type="button" aria-label="Photo {{ loop.index }}"{% if loop.first %} class="on"{% endif %}></button>{% endfor %}</div>{% endif %}
</div>
<script>
(function(){
 var box=document.getElementById('rcbcSlides'); if(!box) return;
 var slides=box.querySelectorAll('.slide'), dots=box.querySelectorAll('.slide-dots button');
 if(slides.length<2) return;
 var i=0, timer=null;
 function show(n){ slides[i].classList.remove('on'); if(dots[i]) dots[i].classList.remove('on');
  i=(n+slides.length)%slides.length;
  slides[i].classList.add('on'); if(dots[i]) dots[i].classList.add('on'); }
 function start(){ if(!timer && !window.matchMedia('(prefers-reduced-motion: reduce)').matches)
  timer=setInterval(function(){ show(i+1); },3000); }
 function stop(){ if(timer){ clearInterval(timer); timer=null; } }
 for(var d=0; d<dots.length; d++){ (function(n){ dots[n].addEventListener('click',function(){ stop(); show(n); start(); }); })(d); }
 box.addEventListener('mouseenter',stop); box.addEventListener('mouseleave',start);
 start();
})();
</script>
{% endif %}
<div class="grid">
{% if is_admin %}<div class="card"><h3>Directory</h3><p>Chungtel min le address kawl.</p><a href="/directory">Directory &rarr;</a></div>{% endif %}
<div class="card"><h3>Church Event</h3><p>Bupi, Youth, CE, Mission le Nubu department events.</p><a href="/church-event">Church Event &rarr;</a></div>
<div class="card"><h3>Church News</h3><p>Thawngpang thar pawl.</p><a href="/church-news">Church News &rarr;</a></div>
<div class="card"><h3>Pathian Bia</h3><p>Thawngtha bia - Pathian bia rel khawh.</p><a href="/pathian-bia">Pathian Bia &rarr;</a></div>
<div class="card"><h3>Caan Ngeitu</h3><p>Pumhnak cio i rian ngeitu pawl.</p><a href="/caan-ngeitu">Caan Ngeitu &rarr;</a></div>
</div>
<div class="card"><h3>Latest News</h3>
{% if news %}{% for n in news[:3] %}<p><strong>{{ n.date }}</strong> - {{ n.title }}</p>{% endfor %}
<p><a href="/church-news">Church News &rarr;</a></p>
{% else %}<p class="empty">Thawng thar a um rih lo.</p>{% endif %}</div>
{% if is_admin %}<div class="card"><h3>Church Logo / Watermark</h3>
{% if has_logo %}<p>Logo a um cang - page vialte background ah watermark in a lang.</p>
<p><img src="/church-logo" alt="Church Logo" style="max-width:160px;max-height:160px;background:#fff;border:1px solid #e5ddd0;border-radius:8px;padding:6px"></p>
{% else %}<p class="empty">Logo a um rih lo - a tanglei form in upload law page vialte background ah watermark in a lang lai.</p>{% endif %}
<form method="post" enctype="multipart/form-data" action="/church-logo/upload">
<label>Logo Photo (JPG, PNG, WebP, GIF, 8 MB tlun lo)</label>
<input name="photo" type="file" accept="image/jpeg,image/png,image/webp,image/gif,.jpg,.jpeg,.png,.webp,.gif" required>
<button class="btn" type="submit">Upload Logo</button></form>
{% if has_logo %}<form method="post" action="/church-logo/delete" onsubmit="return confirm('Logo hi hloh duh taktak maw? Watermark a lang ti lai lo.')" style="margin-top:10px"><button type="submit">Logo Hloh / Remove Logo</button></form>{% endif %}
</div>{% endif %}
""" + BASE_FOOT
    return render_template_string(html, title="Home", active="home", church=CHURCH, news=get_news(), times=get_service_times(),
                            photos=get_gallery_photos())


@app.route("/directory", methods=["GET", "POST"])
def directory():
    # Directory cu admin lawngin hmuh khawh - public ah lang lo
    # (min, address, phone a him lo caah).
    if not is_admin():
        return redirect(url_for("login", next=request.path))
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            sql = ("INSERT INTO members "
                   "(name, address, phone, family, family_members, note) "
                   "VALUES (?,?,?,?,?,?)")
            params = (name, request.form.get("address", "").strip(),
                      request.form.get("phone", "").strip(),
                      request.form.get("family", "").strip(),
                      _family_members_from_form(),
                      request.form.get("note", "").strip())
            try:
                db.execute(sql, params)
                db.commit()
            except Exception:
                # Hlun DB ah family_members column a um lo sual ah
                try:
                    db.rollback()
                except Exception:
                    pass
                init_db()
                db.execute(sql, params)
                db.commit()
        return redirect(url_for("directory"))
    q = request.args.get("q", "").strip()
    try:
        if q:
            like = f"%{q}%"
            raw = db.execute(
                "SELECT * FROM members WHERE name LIKE ? OR address LIKE ? OR phone LIKE ? OR family LIKE ? OR family_members LIKE ? ORDER BY name",
                (like, like, like, like, like),
            ).fetchall()
        else:
            raw = db.execute("SELECT * FROM members ORDER BY name").fetchall()
    except Exception:
        init_db()
        if q:
            like = f"%{q}%"
            raw = db.execute(
                "SELECT * FROM members WHERE name LIKE ? OR address LIKE ? OR phone LIKE ? OR family LIKE ? OR family_members LIKE ? ORDER BY name",
                (like, like, like, like, like),
            ).fetchall()
        else:
            raw = db.execute("SELECT * FROM members ORDER BY name").fetchall()
    rows = [_member_dict(r) for r in raw]
    html = BASE_HEAD + """
<h2>Church Directory</h2>
<div class="card"><h3>Search / Kawl</h3>
<form method="get" class="search">
<input name="q" value="{{ q }}" placeholder="Min, address, phone, chungtel min in kawl...">
<button class="btn" type="submit">Search</button>
{% if q %}<a href="/directory">Clear</a>{% endif %}</form>
<p>{{ rows|length }} entries</p></div>
<div class="card">{% if rows %}<table><tr><th>Name / Min</th><th>Address</th><th>Phone</th><th>Family</th><th>Family Members / Chungtel Min</th><th>Note</th>{% if is_admin %}<th></th>{% endif %}</tr>
{% for r in rows %}<tr><td>{{ r.name }}</td><td>{{ r.address }}</td><td>{{ r.phone }}</td><td>{{ r.family }}</td><td>{% if r.members_list %}<ol class="member-list">{% for m in r.members_list %}<li>{{ m }}</li>{% endfor %}</ol><span class="member-count">{{ r.members_list|length }} members</span>{% else %}<span class="empty">-</span>{% endif %}</td><td>{{ r.note }}</td>
{% if is_admin %}<td><a href="/directory/edit/{{ r.id }}">Edit</a><form method="post" action="/directory/delete/{{ r.id }}" onsubmit="return confirm('Delete?')"><button type="submit">Delete</button></form></td>{% endif %}</tr>{% endfor %}</table>
{% else %}<p class="empty">Directory ah min a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p>{% endif %}</div>
{% if is_admin %}<div class="card"><h3>Add New / Thar Chiah</h3><form method="post">
<label>Name / Min *</label><input name="name" required>
<label>Address</label><input name="address" placeholder="Street, City, NC ZIP">
<label>Phone</label><input name="phone">
<label>Family / Chung Min</label><input name="family" placeholder="e.g. Chung min / Household name">
<label>Family Members / Chungtel Min</label>
<p class="empty">Family tam deuh caah: chungtel pakhat cio caah tlar pakhat ah min pakhat tial. Tlar tam deuh duh ah "+ Member Thar Chap" hmet - a lawng mi tlar cu save a si lo.</p>
<div class="family-rows">{% for i in range(1,6) %}<div class="family-row"><span class="fam-no">{{ i }}.</span><input name="family_member" placeholder="Chungtel min - member {{ i }}"><button type="button" class="remove-family-row">Hloh</button></div>{% endfor %}</div>
<button type="button" class="add-family-row">+ Member Thar Chap / Add Family Member</button>
<label>Note</label><textarea name="note" rows="2"></textarea>
<button class="btn" type="submit">Add to Directory</button></form></div>{% endif %}
""" + BASE_FOOT
    return render_template_string(html, title="Directory", active="directory", church=CHURCH, rows=rows, q=q)


@app.route("/directory/delete/<int:member_id>", methods=["POST"])
@login_required
def delete_member(member_id):
    db = get_db()
    db.execute("DELETE FROM members WHERE id=?", (member_id,))
    db.commit()
    return redirect(url_for("directory"))


DIRECTORY_EDIT_HTML = """
<h2>Edit Directory / Directory Remh</h2>
<div class="card"><h3>{{ member.name }}</h3>
<form method="post">
<label>Name / Min *</label>
<input name="name" required value="{{ member.name }}">
<label>Address</label>
<input name="address" value="{{ member.address }}" placeholder="Street, City, NC ZIP">
<label>Phone</label>
<input name="phone" value="{{ member.phone }}">
<label>Family / Chungkhar min</label>
<input name="family" value="{{ member.family }}" placeholder="e.g. Chungkhar min / Household name">
<label>Family Members / Chungtel Min</label>
<p class="empty">Chungtel pakhat cio caah tlar pakhat ah min pakhat.
Chap duh ah "+ Member Thar Chap" hmet; hloh duh mi tlar cu
"Hloh" hmet asilole a lawng in chiata law Save hmet.</p>
<div class="family-rows">{% for m in member.members_list %}<div class="family-row"><span class="fam-no">{{ loop.index }}.</span><input name="family_member" value="{{ m }}" placeholder="Chungtel min"><button type="button" class="remove-family-row">Hloh</button></div>{% endfor %}<div class="family-row"><span class="fam-no">{{ member.members_list|length + 1 }}.</span><input name="family_member" placeholder="Chungtel min thar"><button type="button" class="remove-family-row">Hloh</button></div></div>
<button type="button" class="add-family-row">+ Member Thar Chap / Add Family Member</button>
<label>Note</label>
<textarea name="note" rows="2">{{ member.note }}</textarea>
<button class="btn" type="submit">Save / Fim</button>
<a href="/directory">Cancel / Kir Than</a>
</form></div>
"""


@app.route("/directory/edit/<int:member_id>", methods=["GET", "POST"])
@login_required
def edit_member(member_id):
    db = get_db()
    try:
        row = db.execute("SELECT * FROM members WHERE id=?",
                         (member_id,)).fetchone()
    except Exception:
        init_db()
        row = db.execute("SELECT * FROM members WHERE id=?",
                         (member_id,)).fetchone()
    if row is None:
        return redirect(url_for("directory"))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            sql = ("UPDATE members SET name=?, address=?, phone=?, "
                   "family=?, family_members=?, note=? WHERE id=?")
            params = (name, request.form.get("address", "").strip(),
                      request.form.get("phone", "").strip(),
                      request.form.get("family", "").strip(),
                      _family_members_from_form(),
                      request.form.get("note", "").strip(), member_id)
            try:
                db.execute(sql, params)
                db.commit()
            except Exception:
                try:
                    db.rollback()
                except Exception:
                    pass
                init_db()
                db.execute(sql, params)
                db.commit()
        return redirect(url_for("directory"))
    html = BASE_HEAD + DIRECTORY_EDIT_HTML + BASE_FOOT
    return render_template_string(
        html, title="Edit Directory", active="directory", church=CHURCH,
        member=_member_dict(row))


def event_page(title, active, category, heading):
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        ev_title = request.form.get("title", "").strip()
        ev_date = request.form.get("date", "").strip()
        if not ev_date:
            ev_date = date.today().isoformat()
        if ev_title:
            sql = ("INSERT INTO events (category, date, title, time, place, note) "
                   "VALUES (?,?,?,?,?,?)")
            params = (category, ev_date, ev_title,
                      request.form.get("time", "").strip(),
                      request.form.get("place", "").strip(),
                      request.form.get("note", "").strip())
            try:
                db.execute(sql, params)
                db.commit()
            except sqlite3.OperationalError:
                init_db()
                db.execute(sql, params)
                db.commit()
            # Event ni a um mi thla ah kal colh - calendar mark kha
            # le table kha a hmuh colh nak ding
            try:
                y, m = int(ev_date[:4]), int(ev_date[5:7])
                if not 1 <= m <= 12:
                    raise ValueError
                return redirect(f"{request.path}?year={y}&month={m}")
            except (ValueError, IndexError):
                return redirect(request.path)
        return redirect(request.path)
    events = get_events(category)
    today = date.today()
    try:
        year = int(request.args.get("year", today.year))
        month = int(request.args.get("month", today.month))
        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        year, month = today.year, today.month
    cal = build_calendar(year, month, events)
    all_events = sorted_events(events)
    prefix = f"{year:04d}-{month:02d}-"
    month_events = [ev for ev in all_events if ev["date"].startswith(prefix)]
    html = BASE_HEAD + f"<h2>{heading}</h2>" + CALENDAR_HTML + BASE_FOOT
    return render_template_string(
        html, title=title, active=active, church=CHURCH,
        cal=cal, event_list=all_events, month_events=month_events,
        request_path=request.path, today=today.isoformat(),
    )


@app.route("/bupi-event", methods=["GET", "POST"])
def bupi_event():
    return event_page("Bupi Event", "bupi", "bupi", "Bupi Event")


@app.route("/youth-event", methods=["GET", "POST"])
def youth_event():
    return event_page("Youth Event", "youth", "youth", "Youth Event")


@app.route("/ce-event", methods=["GET", "POST"])
def ce_event():
    return event_page("CE Event", "ce", "ce", "CE Event - Christian Education")


@app.route("/mission-event", methods=["GET", "POST"])
def mission_event():
    return event_page("Mission Event", "mission", "mission", "Mission Event")


@app.route("/nubu-event", methods=["GET", "POST"])
def nubu_event():
    return event_page("Nubu Event", "nubu", "nubu", "Nubu Event - Women")



# Church Event hub: department vialte hmunkhat ah; a tangah
# tuthla i department vialte i a biapi mi ni fonh mi table.
EVENT_DEPARTMENTS = [
    {"cat": "bupi", "label": "Bupi", "url": "/bupi-event",
     "desc": "Khrihfabu pumpi (Bupi) event pawl."},
    {"cat": "youth", "label": "Youth", "url": "/youth-event",
     "desc": "Mino (Youth) department event pawl."},
    {"cat": "ce", "label": "CE", "url": "/ce-event",
     "desc": "Christian Education department event pawl."},
    {"cat": "mission", "label": "Mission", "url": "/mission-event",
     "desc": "Mission department event pawl."},
    {"cat": "nubu", "label": "Nubu", "url": "/nubu-event",
     "desc": "Nubu (Women) department event pawl."},
]


@app.route("/church-event")
def church_event():
    today = date.today()
    try:
        year = int(request.args.get("year", today.year))
        month = int(request.args.get("month", today.month))
        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        year, month = today.year, today.month
    merged = {}
    for dept in EVENT_DEPARTMENTS:
        for day, evs in get_events(dept["cat"]).items():
            for ev in evs:
                merged.setdefault(day, []).append(ev)
    cal = build_calendar(year, month, merged)
    prefix = f"{year:04d}-{month:02d}-"
    combined = []
    for dept in EVENT_DEPARTMENTS:
        for ev in sorted_events(get_events(dept["cat"])):
            if ev["date"].startswith(prefix):
                row = dict(ev)
                row["dept"] = dept["label"]
                combined.append(row)
    combined.sort(key=lambda e: e["date"])
    html = BASE_HEAD + """
<h2>Church Event</h2>
<div class="card"><p>Khrihfabu pumpi le department cio i event pawl.
Department na duh mi thim law a calendar le a event pawl a lang lai.</p></div>
<div class="grid">
{% for d in departments %}<div class="card"><h3>{{ d.label }}</h3><p>{{ d.desc }}</p><a href="{{ d.url }}">{{ d.label }} Event &rarr;</a></div>
{% endfor %}</div>
<div class="card"><h3>{{ cal.month_name }} {{ cal.year }}</h3>
<div class="cal-nav"><a href="?year={{cal.prev_y}}&month={{cal.prev_m}}">&larr; Previous</a>
<span>{{ cal.month_name }} {{ cal.year }}</span>
<a href="?year={{cal.next_y}}&month={{cal.next_m}}">Next &rarr;</a></div>
<table class="cal"><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>
{% for week in cal.weeks %}<tr>{% for d in week %}
{% if d is none %}<td class="empty"></td>{% else %}<td><strong>{{ d.day }}</strong>
{% for ev in d.events %}<div class="ev">{{ ev.title }}{% if ev.time %}<br>{{ ev.time }}{% endif %}{% if ev.note %}<br><em>{{ ev.note }}</em>{% endif %}</div>{% endfor %}</td>{% endif %}
{% endfor %}</tr>{% endfor %}</table></div>
<div class="card"><h3>A Biapi mi Ni / Important Days - {{ cal.month_name }} {{ cal.year }}</h3>
{% if month_events %}<div class="table-wrap"><table>
<tr><th>Ni / Date</th><th>Department</th><th>Event</th><th>Caan / Time</th><th>Hmun / Place</th></tr>
{% for ev in month_events %}<tr><td>{{ ev.date }}</td><td>{{ ev.dept }}</td><td>{{ ev.title }}</td><td>{{ ev.time }}</td><td>{{ ev.place }}</td></tr>
{% endfor %}</table></div>
{% else %}<p class="empty">{{ cal.month_name }} ah event a um rih lo.</p>{% endif %}</div>
""" + BASE_FOOT
    return render_template_string(
        html, title="Church Event", active="church-event", church=CHURCH,
        departments=EVENT_DEPARTMENTS, month_events=combined, cal=cal,
    )


@app.route("/events/delete/<int:event_id>", methods=["POST"])
@login_required
def delete_event(event_id):
    db = get_db()
    try:
        db.execute("DELETE FROM events WHERE id=?", (event_id,))
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.execute("DELETE FROM events WHERE id=?", (event_id,))
        db.commit()
    nxt = request.form.get("next", "").strip()
    if nxt.startswith("/"):
        return redirect(nxt)
    return redirect(url_for("bupi_event"))


LEADERS_PAGE_HTML = """
<h2>Church Leaders / Khrihfabu Hruaitu</h2>
{% if leaders %}<div class="grid">{% for p in leaders %}
<div class="card leader-card">
{% if p.has_photo and p.id %}<img class="leader-photo" src="/leader-photo/{{ p.id }}" alt="{{ p.name }}">
{% else %}<div class="leader-placeholder">{{ p.initial }}</div>{% endif %}
<h3>{{ p.name }}</h3>
{% if p.position %}<p><strong>{{ p.position }}</strong></p>{% endif %}
{% if p.phone %}<p>Phone: {{ p.phone }}</p>{% endif %}
{% if p.email %}<p>Email: {{ p.email }}</p>{% endif %}
{% if p.bio %}<p style="white-space:pre-line">{{ p.bio }}</p>{% endif %}
{% if is_admin and p.id %}<div class="leader-actions"><a href="/church-leaders/edit/{{ p.id }}">Edit</a>
<form method="post" action="/church-leaders/delete/{{ p.id }}" onsubmit="return confirm('Hi leader hi delete duh taktak maw?')"><button type="submit">Delete</button></form></div>
<details class="edit-box"><summary>Edit / Remh (hitta zong)</summary>
<form method="post" enctype="multipart/form-data" action="/church-leaders/edit/{{ p.id }}" style="text-align:left">
<label>Name / Min *</label><input name="name" required value="{{ p.name }}">
<label>Position / Rian</label>
<select name="position">{% for pos in positions %}<option value="{{ pos }}" {% if p.position == pos %}selected{% endif %}>{{ pos }}</option>{% endfor %}<option value="Other" {% if p.position and p.position not in positions %}selected{% endif %}>Other</option></select>
<label>Other Position (Other na thim ahcun tial)</label><input name="position_other" value="{% if p.position and p.position not in positions %}{{ p.position }}{% endif %}">
<label>Phone</label><input name="phone" value="{{ p.phone }}">
<label>Email</label><input name="email" value="{{ p.email }}">
<label>Bio / Konglam</label><textarea name="bio" rows="4">{{ p.bio }}</textarea>
<label>Picture / Hmanthlak (thar na thlak duh ah lawng thim)</label><input name="photo" type="file" accept="image/jpeg,image/png,image/webp,image/gif,.jpg,.jpeg,.png,.webp,.gif">
{% if p.has_photo %}<label><input type="checkbox" name="remove_photo" style="width:auto"> Remove Photo / Hmanthlak Hloh</label>{% endif %}
<label>Sort Order / A No.</label><input name="sort_order" type="number" value="{{ p.sort_order }}">
<button class="btn" type="submit">Save / Fim</button></form></details>{% endif %}
</div>{% endfor %}</div>
{% else %}<div class="card"><p class="empty">Church leader min a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p></div>{% endif %}
{% if is_admin %}<div class="card"><h3>Leader Thar Chiah / Add Leader</h3>
<p class="empty">hika form in Min, Position
le Picture chiah law a save cang lai, website na restart zongah
a tlau lai lo. Photo cu JPG, PNG, WebP, GIF, 8 MB tlun lo ding.</p>
<form method="post" enctype="multipart/form-data">
<label>Name / Min *</label>
<input name="name" required placeholder="e.g. Pastor min">
<label>Position / Rian</label>
<select name="position">{% for pos in positions %}<option value="{{ pos }}">{{ pos }}</option>{% endfor %}<option value="Other">Other</option></select>
<label>Other Position (Other na thim ahcun tial)</label>
<input name="position_other" placeholder="Position dang tial...">
<label>Phone</label><input name="phone">
<label>Email</label><input name="email">
<label>Bio / Konglam</label>
<textarea name="bio" rows="4" placeholder="Leader konglam tawi tial..."></textarea>
<label>Picture / Hmanthlak (photo)</label>
<input name="photo" type="file" accept="image/jpeg,image/png,image/webp,image/gif,.jpg,.jpeg,.png,.webp,.gif">
<label>Sort Order / A No.</label>
<input name="sort_order" type="number" value="0">
<button class="btn" type="submit">Add Leader / Leader Thar Chiah</button>
</form></div>{% endif %}
"""

LEADER_EDIT_HTML = """
<h2>Edit Leader / Leader Remh</h2>
<div class="card leader-card">
{% if leader.has_photo %}<img class="leader-photo" src="/leader-photo/{{ leader.id }}" alt="{{ leader.name }}">
{% else %}<div class="leader-placeholder">{{ leader.initial }}</div>{% endif %}
<h3>{{ leader.name }}</h3>
{% if leader.position %}<p><strong>{{ leader.position }}</strong></p>{% endif %}
</div>
<div class="card"><h3>Leader Remh / Edit Leader</h3>
<form method="post" enctype="multipart/form-data">
<label>Name / Min *</label>
<input name="name" required value="{{ leader.name }}">
<label>Position / Rian</label>
<select name="position">{% for pos in positions %}<option value="{{ pos }}" {% if leader.position == pos %}selected{% endif %}>{{ pos }}</option>{% endfor %}<option value="Other" {% if leader.position and leader.position not in positions %}selected{% endif %}>Other</option></select>
<label>Other Position (Other na thim ahcun tial)</label>
<input name="position_other" value="{% if leader.position and leader.position not in positions %}{{ leader.position }}{% endif %}">
<label>Phone</label><input name="phone" value="{{ leader.phone }}">
<label>Email</label><input name="email" value="{{ leader.email }}">
<label>Bio / Konglam</label>
<textarea name="bio" rows="4">{{ leader.bio }}</textarea>
<label>Picture / Hmanthlak (thar na thlak duh ah lawng thim; a hlun mi a tang lai)</label>
<input name="photo" type="file" accept="image/jpeg,image/png,image/webp,image/gif,.jpg,.jpeg,.png,.webp,.gif">
{% if leader.has_photo %}<label><input type="checkbox" name="remove_photo" style="width:auto"> Remove Photo / Hmanthlak Hloh</label>{% endif %}
<label>Sort Order / A No.</label>
<input name="sort_order" type="number" value="{{ leader.sort_order }}">
<button class="btn" type="submit">Save / Fim</button>
<a href="/church-leaders">Cancel / Kir Than</a>
</form></div>
"""

@app.route("/church-leaders", methods=["GET", "POST"])
def church_leaders():
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        data = _leader_form_data()
        if data["name"]:
            photo_data, photo_mime, _err = _read_leader_photo(
                request.files.get("photo"))
            if _err:
                photo_data, photo_mime = None, ""
            sql = ("INSERT INTO leaders (name, position, phone, email, bio, "
                   "photo_data, photo_mimetype, sort_order) "
                   "VALUES (?,?,?,?,?,?,?,?)")
            params = (data["name"], data["position"], data["phone"],
                      data["email"], data["bio"], photo_data, photo_mime,
                      data["sort_order"])
            try:
                db.execute(sql, params)
                db.commit()
            except sqlite3.OperationalError:
                init_db()
                db.execute(sql, params)
                db.commit()
        return redirect(url_for("church_leaders"))
    html = BASE_HEAD + LEADERS_PAGE_HTML + BASE_FOOT
    return render_template_string(
        html, title="Church Leaders", active="leaders", church=CHURCH,
        leaders=get_leaders(), positions=LEADER_POSITIONS)


@app.route("/church-leaders/edit/<int:leader_id>", methods=["GET", "POST"])
@login_required
def edit_leader(leader_id):
    db = get_db()
    try:
        row = db.execute("SELECT * FROM leaders WHERE id=?",
                         (leader_id,)).fetchone()
    except sqlite3.OperationalError:
        init_db()
        row = db.execute("SELECT * FROM leaders WHERE id=?",
                         (leader_id,)).fetchone()
    if row is None:
        return redirect(url_for("church_leaders"))
    if request.method == "POST":
        data = _leader_form_data()
        if data["name"]:
            remove = request.form.get("remove_photo", "") in ("on", "1", "true")
            new_data, new_mime, _err = _read_leader_photo(
                request.files.get("photo"))
            if _err:
                new_data, new_mime = None, ""
            if remove:
                photo_data, photo_mime = None, ""
            elif new_data is not None:
                photo_data, photo_mime = new_data, new_mime
            else:
                photo_data = row["photo_data"]
                photo_mime = row["photo_mimetype"] or ""
            db.execute(
                "UPDATE leaders SET name=?, position=?, phone=?, email=?, "
                "bio=?, photo_data=?, photo_mimetype=?, sort_order=? "
                "WHERE id=?",
                (data["name"], data["position"], data["phone"],
                 data["email"], data["bio"], photo_data, photo_mime,
                 data["sort_order"], leader_id))
            db.commit()
        return redirect(url_for("church_leaders"))
    leader = dict(row)
    leader["has_photo"] = bool(leader.get("photo_data"))
    leader.pop("photo_data", None)
    leader.pop("photo_mimetype", None)
    nm = (leader.get("name") or "").strip()
    leader["initial"] = nm[:1].upper() if nm else "?"
    html = BASE_HEAD + LEADER_EDIT_HTML + BASE_FOOT
    return render_template_string(
        html, title="Edit Leader", active="leaders", church=CHURCH,
        leader=leader, positions=LEADER_POSITIONS)


@app.route("/church-leaders/delete/<int:leader_id>", methods=["POST"])
@login_required
def delete_leader(leader_id):
    db = get_db()
    try:
        db.execute("DELETE FROM leaders WHERE id=?", (leader_id,))
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.execute("DELETE FROM leaders WHERE id=?", (leader_id,))
        db.commit()
    return redirect(url_for("church_leaders"))


@app.route("/leader-photo/<int:leader_id>")
def leader_photo(leader_id):
    db = get_db()
    try:
        row = db.execute(
            "SELECT photo_data, photo_mimetype FROM leaders WHERE id=?",
            (leader_id,)).fetchone()
    except sqlite3.OperationalError:
        init_db()
        row = db.execute(
            "SELECT photo_data, photo_mimetype FROM leaders WHERE id=?",
            (leader_id,)).fetchone()
    if row is None or not row["photo_data"]:
        return ("Not Found", 404)
    data = bytes(row["photo_data"])
    mime = row["photo_mimetype"] or _detect_image_mimetype(data) \
        or "application/octet-stream"
    return send_file(io.BytesIO(data), mimetype=mime)


@app.route("/church-news", methods=["GET", "POST"])
def church_news():
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()
        news_date = request.form.get("date", "").strip()
        if not news_date:
            news_date = date.today().isoformat()
        if title:
            try:
                db.execute(
                    "INSERT INTO news (title, body, date) VALUES (?,?,?)",
                    (title, body, news_date),
                )
                db.commit()
            except sqlite3.OperationalError:
                init_db()
                db.execute(
                    "INSERT INTO news (title, body, date) VALUES (?,?,?)",
                    (title, body, news_date),
                )
                db.commit()
        return redirect(url_for("church_news"))
    html = BASE_HEAD + """
<h2>Church News / Khrihfabu thawng</h2>
{% if news %}{% for n in news %}
<div class="card"><h3>{{ n.title }}</h3>
{% if n.date %}<p><small>{{ n.date }}</small></p>{% endif %}
<p style="white-space:pre-line">{{ n.body }}</p>
{% if is_admin %}<form method="post" action="/church-news/delete/{{ n.id }}"
onsubmit="return confirm('Hi thawng thar hi delete duh taktak maw?')">
<button type="submit">Delete</button></form>{% endif %}</div>
{% endfor %}{% else %}<div class="card"><p class="empty">Thuthang thar a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p></div>{% endif %}
{% if is_admin %}<div class="card"><h3>Thawng Thar Chiah / Add News</h3>
<p class="empty">Hika form in tial law save, website na restart zongah a tlau lai lo.</p>
<form method="post">
<label>Title / Title *</label>
<input name="title" required placeholder="e.g. Sunday Worship Thawngthanh">
<label>Date / Ni *</label>
<input name="date" type="date" value="{{ today }}" required>
<label>Thawngthanh / News</label>
<textarea name="body" rows="6" placeholder="Thawngthar paohpaoh hika hin tial..."></textarea>
<button class="btn" type="submit">Add News / Thawng Thar Chiah</button>
</form></div>{% endif %}
<div class="card"><h3>Church Activity Pictures / Khrihfabu Cawlcanghnak Hmanthlak</h3>
{% if gallery %}<div class="gallery">{% for g in gallery %}<figure class="g-item"><a href="/gallery-photo/{{ g.id }}" target="_blank"><img src="/gallery-photo/{{ g.id }}" alt="{{ g.caption }}" loading="lazy"></a>{% if g.caption %}<figcaption>{{ g.caption }}</figcaption>{% endif %}{% if is_admin %}<form method="post" action="/gallery/delete/{{ g.id }}" onsubmit="return confirm('Hi hmanthlak hi delete duh taktak maw?')"><button type="submit">Delete</button></form>{% endif %}</figure>{% endfor %}</div>
{% else %}<p class="empty">Hmanthlak a um rih lo.{% if is_admin %} A tanglei form in activity hmanthlak upload.{% endif %}</p>{% endif %}
{% if is_admin %}<form method="post" enctype="multipart/form-data" action="/gallery/upload" style="margin-top:12px">
<label>Picture (JPG, PNG, WebP, GIF, 8 MB tlun lo)</label>
<input name="photo" type="file" accept="image/jpeg,image/png,image/webp,image/gif,.jpg,.jpeg,.png,.webp,.gif" required>
<label>Caption / Hmanthlak kong (duh ahcun)</label>
<input name="caption" placeholder="e.g. 2026 Church Picnic">
<button class="btn" type="submit">Upload Picture / Hmanthlak Thun</button></form>{% endif %}</div>
<div class="card"><h3>RCBC YouTube</h3>
{% if youtube_channel %}<p><a class="btn yt-btn" href="{{ youtube_channel }}" target="_blank" rel="noopener">&#9654; RCBC YouTube Channel</a></p>{% endif %}
{% if videos %}{% for v in videos %}<div class="video-box"><p><strong>{{ v.title }}</strong></p><div class="video-wrap"><iframe src="https://www.youtube-nocookie.com/embed/{{ v.video_id }}" title="{{ v.title }}" loading="lazy" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>{% if is_admin %}<form method="post" action="/videos/delete/{{ v.id }}" onsubmit="return confirm('Hi video hi delete duh taktak maw?')" style="margin-top:8px"><button type="submit">Delete</button></form>{% endif %}</div>{% endfor %}
{% else %}<p class="empty">Video a um rih lo.{% if is_admin %} A tanglei form in YouTube video link chiah.{% endif %}</p>{% endif %}
{% if is_admin %}<form method="post" action="/youtube-channel">
<label>YouTube Channel Link</label>
<input name="channel_url" type="url" value="{{ youtube_channel }}" placeholder="https://www.youtube.com/@RCBC...">
<button class="btn" type="submit">Channel Link Save</button></form>
<form method="post" action="/videos/add" style="margin-top:16px">
<label>Video Title</label>
<input name="title" placeholder="e.g. Sunday Pumhnak - Nov 8, 2026">
<label>YouTube Video Link *</label>
<input name="url" type="url" required placeholder="https://www.youtube.com/watch?v=...">
<button class="btn" type="submit">Add Video / Video Chiah</button></form>{% endif %}</div>
""" + BASE_FOOT
    return render_template_string(
        html, title="Church News", active="news", church=CHURCH,
        news=get_news(), today=date.today().isoformat(),
        gallery=get_gallery_photos(), videos=get_videos(),
        youtube_channel=get_youtube_channel(),
    )


@app.route("/church-news/delete/<int:news_id>", methods=["POST"])
@login_required
def delete_news(news_id):
    db = get_db()
    db.execute("DELETE FROM news WHERE id=?", (news_id,))
    db.commit()
    return redirect(url_for("church_news"))


# ------------------------------------------------------------------
# Church Activity Pictures (Gallery) + YouTube + About Us
# ------------------------------------------------------------------

def get_gallery_photos():
    db = get_db()
    try:
        rows = db.execute(
            "SELECT id, caption FROM gallery_photos ORDER BY id DESC"
        ).fetchall()
    except Exception:
        return []
    return [{"id": r["id"], "caption": r["caption"] or ""} for r in rows]


def get_videos():
    db = get_db()
    try:
        rows = db.execute(
            "SELECT * FROM videos ORDER BY id DESC"
        ).fetchall()
    except Exception:
        return []
    return [dict(r) for r in rows]


def _get_setting(key, default=""):
    db = get_db()
    try:
        row = db.execute(
            "SELECT value FROM settings WHERE key=?", (key,)
        ).fetchone()
    except Exception:
        return default
    return (row[0] if row and row[0] else default)


def _set_setting(key, value):
    db = get_db()
    db.execute(
        "INSERT OR REPLACE INTO settings (key, value) VALUES (?,?)",
        (key, value),
    )
    db.commit()


def get_youtube_channel():
    return _get_setting("youtube_channel_url", "")


def youtube_video_id(url):
    import re
    if not url:
        return ""
    for pat in (r"youtube\.com/watch\?[^#]*v=([\w-]{6,})",
                r"youtu\.be/([\w-]{6,})",
                r"youtube\.com/(?:embed|shorts|live)/([\w-]{6,})"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return ""


@app.route("/gallery/upload", methods=["POST"])
@login_required
def gallery_upload():
    data, mime, err = _read_leader_photo(request.files.get("photo"))
    if data:
        db = get_db()
        db.execute(
            "INSERT INTO gallery_photos (caption, data, mimetype, created) "
            "VALUES (?,?,?,?)",
            (request.form.get("caption", "").strip(), data, mime,
             date.today().isoformat()),
        )
        db.commit()
    return redirect(url_for("church_news"))


@app.route("/gallery-photo/<int:photo_id>")
def gallery_photo(photo_id):
    db = get_db()
    row = db.execute(
        "SELECT data, mimetype FROM gallery_photos WHERE id=?",
        (photo_id,),
    ).fetchone()
    if not row or not row[0]:
        return ("", 404)
    return send_file(io.BytesIO(bytes(row[0])),
                     mimetype=row[1] or "image/jpeg")


@app.route("/gallery/delete/<int:photo_id>", methods=["POST"])
@login_required
def gallery_delete(photo_id):
    db = get_db()
    db.execute("DELETE FROM gallery_photos WHERE id=?", (photo_id,))
    db.commit()
    return redirect(url_for("church_news"))


@app.route("/youtube-channel", methods=["POST"])
@login_required
def youtube_channel_save():
    url = request.form.get("channel_url", "").strip()
    if url and not url.startswith(("http://", "https://")):
        url = "https://" + url
    _set_setting("youtube_channel_url", url)
    return redirect(url_for("church_news"))


@app.route("/videos/add", methods=["POST"])
@login_required
def videos_add():
    url = request.form.get("url", "").strip()
    vid = youtube_video_id(url)
    if vid:
        db = get_db()
        db.execute(
            "INSERT INTO videos (title, url, video_id, created) "
            "VALUES (?,?,?,?)",
            (request.form.get("title", "").strip() or "RCBC Video",
             url, vid, date.today().isoformat()),
        )
        db.commit()
    return redirect(url_for("church_news"))


@app.route("/videos/delete/<int:video_id>", methods=["POST"])
@login_required
def videos_delete(video_id):
    db = get_db()
    db.execute("DELETE FROM videos WHERE id=?", (video_id,))
    db.commit()
    return redirect(url_for("church_news"))


DEFAULT_ABOUT = (
    "Raleigh Chin Baptist Church (RCBC) cu Raleigh, North "
    "Carolina ah a um mi Chin khrihfabu a si. Pathian thangthat, "
    "bia cawnpiak le i hawikomhnak in kan pum tawn.\n\n"
    "Pumhnak Caan / Service Times:\n"
    "Friday 7:00 PM\n"
    "Sunday 1:00 PM - 3:00 PM\n\n"
    "Motto: \u201cAnd ye shall know the truth, and the truth "
    "shall make you free.\u201d - John 8:32\n\n"
    "Mi vialte kan in don hna - ra leng mang uh!"
)


def _valid_url(u):
    return u.startswith("http://") or u.startswith("https://")


def get_social_links():
    return {
        "facebook": _get_setting("facebook_url", ""),
        "instagram": _get_setting("instagram_url", ""),
    }


@app.route("/about/social", methods=["POST"])
def about_social():
    if not is_admin():
        return redirect(url_for("login", next="/about"))
    for key, field in (("facebook_url", "facebook_url"),
                       ("instagram_url", "instagram_url")):
        url = request.form.get(field, "").strip()
        _set_setting(key, url if _valid_url(url) else "")
    return redirect(url_for("about"))


def contact_config():
    to = os.environ.get("RCBC_CONTACT_TO", "").strip()
    user = os.environ.get("RCBC_SMTP_USER", "").strip() or to
    pw = os.environ.get("RCBC_SMTP_PASS", "").strip()
    return {"to": to, "user": user, "pw": pw,
            "on": bool(to and user and pw)}


_contact_last = {}


@app.route("/contact", methods=["POST"])
def contact_send():
    import smtplib as _smtp
    from email.message import EmailMessage as _EM
    back = url_for("about")
    if request.form.get("website", ""):
        return redirect(back + "?sent=1#contact")
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    topic = request.form.get("topic", "Message").strip()
    if topic not in ("Message", "Prayer Request"):
        topic = "Message"
    message = request.form.get("message", "").strip()
    email_ok = ("@" in email and "." in email.split("@")[-1]
                and " " not in email and len(email) <= 120)
    if not (name and email_ok and message) or len(message) > 4000:
        return redirect(back + "?sent=0#contact")
    now = _gh_time.time()
    if now - _contact_last.get(request.remote_addr or "", 0) < 30:
        return redirect(back + "?sent=0#contact")
    _contact_last[request.remote_addr or ""] = now
    cfg = contact_config()
    if not cfg["on"]:
        print("Contact form: SMTP env var a um lo (RCBC_CONTACT_TO / "
              "RCBC_SMTP_USER / RCBC_SMTP_PASS).", flush=True)
        return redirect(back + "?sent=0#contact")
    msg = _EM()
    msg["From"] = cfg["user"]
    msg["To"] = cfg["to"]
    msg["Reply-To"] = email
    msg["Subject"] = "[RCBC Website] " + topic + " - " + name
    msg.set_content(
        "RCBC website (rcbcnc.com) About page contact form in a ra mi:\n\n"
        "Min / Name: " + name + "\n"
        "Email: " + email + "\n"
        "Phone: " + (phone or "-") + "\n"
        "Topic: " + topic + "\n\n"
        "Thawng / Message:\n" + message + "\n")
    try:
        with _smtp.SMTP("smtp.gmail.com", 587, timeout=30) as s:
            s.starttls()
            s.login(cfg["user"], cfg["pw"])
            s.send_message(msg)
        print("Contact form: email kuat a tling (" + topic + ").",
              flush=True)
    except Exception as e:
        print("Contact form kuat a tling lo:", e, flush=True)
        return redirect(back + "?sent=0#contact")
    return redirect(back + "?sent=1#contact")


def get_about_text():
    return _get_setting("about_text", "") or DEFAULT_ABOUT


DEFAULT_FOOTER_TEXT = "\u00a9 2026 RCBC"


def get_footer_text():
    return _get_setting("footer_text", "") or DEFAULT_FOOTER_TEXT



BACKUP_HTML = """
{% if gh_on %}<div class="card">
<h2>GitHub Auto-Backup: ON</h2>
<p>Data cu GitHub private repo <strong>{{ gh_repo }}</strong> ah amah tein
a fim peng - deploy / restart in data a tlau ti lai lo, a lawng a si
ahcun amah tein a kir lai.
{% if gh_at %}<br>A hnu bik auto-backup ni: {{ gh_at }}{% endif %}</p>
{% if gh_pending %}<p class="err-note">Backup pending: edit thar a um rih — a tang i button in atu backup khawh a si.</p>{% endif %}
{% if gh_result %}<p class="ok-note">A hnu bik backup try: {{ gh_result }}</p>{% endif %}
<form method="post" action="/backup/github-now"><button class="btn" type="submit">GitHub Ah Atu Backup Tuah / Backup Now</button></form>
</div>
{% endif %}
<div class="card">
<h2>Backup - Data Fimnak</h2>
<p>Post cia mi (Directory, News, Event, Leaders, Photo...) vialte cu database
pakhat ah an um. Code edit / deploy na tuah hlan ah <strong>Backup Download</strong>
hmet law file kha na laptop ah fim. Live site i data a tlau sual ahcun
<strong>Restore</strong> in cu file in na lak kir khawh lai.</p>
<p><a class="btn" href="/backup/download">Backup Download</a></p>
</div>
{% if is_super %}<div class="card">
<h2>Restore (Super Admin lawng)</h2>
<p class="empty">Backup file (.db) thim law Restore hmet. Atu um mi data vialte
cu backup file i mi in an thlak dih lai. A hlun mi cu church_directory.db.safety
ah a um peng lai (kir than khawh a si).</p>
<form method="post" action="/backup/restore" enctype="multipart/form-data"
 onsubmit="return confirm('Atu data vialte cu backup in thlak dih a si lai - peh maw?')">
<label>Backup File (.db)</label>
<input type="file" name="backup_file" accept=".db" required>
<button class="btn" type="submit">Restore</button></form></div>{% endif %}
"""


@app.route("/backup")
@login_required
def backup_page():
    if (_gh_token() and _gh_state.get("dirty")
            and _gh_time.time() - _gh_state.get("since", 0) > 30):
        try:
            _gh_upload_backup()
            _gh_state["dirty"] = False
            _gh_state["last_result"] = ("A tling - "
                                        + date.today().isoformat())
            print("GitHub auto-backup (Backup page): a tling.",
                  flush=True)
        except Exception as e:
            _gh_state["last_result"] = "A tling lo: " + str(e)
            print("GitHub auto-backup (Backup page) a tling lo:", e,
                  flush=True)
    html = (BASE_HEAD + '<section class="page-card">' + BACKUP_HTML
            + "</section>" + BASE_FOOT)
    return render_template_string(
        html, church=CHURCH, gh_on=bool(_gh_token()),
        gh_repo=GH_BACKUP_REPO, gh_at=_get_setting("gh_backup_at", ""),
        gh_pending=bool(_gh_state.get("dirty")),
        gh_result=_gh_state.get("last_result", ""))


@app.route("/backup/github-now", methods=["POST"])
@login_required
def backup_github_now():
    try:
        _gh_upload_backup()
        _gh_state["dirty"] = False
        _gh_state["last_result"] = ("A tling - "
                                    + date.today().isoformat())
        print("GitHub auto-backup (Backup Now): a tling.", flush=True)
    except Exception as e:
        _gh_state["last_result"] = "A tling lo: " + str(e)
        print("GitHub auto-backup (Backup Now) a tling lo:", e,
              flush=True)
    return redirect(url_for("backup_page"))


@app.route("/backup/download")
@login_required
def backup_download():
    tmp_path = DATABASE + ".tmp"
    if os.path.exists(tmp_path):
        os.remove(tmp_path)
    src = sqlite3.connect(DATABASE)
    dst = sqlite3.connect(tmp_path)
    src.backup(dst)
    dst.close()
    src.close()
    with open(tmp_path, "rb") as fh:
        data = fh.read()
    os.remove(tmp_path)
    return send_file(
        io.BytesIO(data), mimetype="application/octet-stream",
        as_attachment=True,
        download_name="rcbc-backup-" + date.today().isoformat() + ".db")


@app.route("/backup/restore", methods=["POST"])
@login_required
def backup_restore():
    if not is_super_admin():
        return redirect(url_for("backup_page"))
    f = request.files.get("backup_file")
    if not f or not f.filename:
        return redirect(url_for("backup_page"))
    raw = f.read()
    ok = raw[:16] == b"SQLite format 3\x00"
    if ok:
        probe_path = DATABASE + ".probe"
        try:
            with open(probe_path, "wb") as fh:
                fh.write(raw)
            probe = sqlite3.connect(probe_path)
            tables = {r[0] for r in probe.execute(
                "SELECT name FROM sqlite_master WHERE type='table'")}
            probe.close()
            ok = {"members", "settings", "news"}.issubset(tables)
        except Exception:
            ok = False
        if os.path.exists(probe_path):
            os.remove(probe_path)
    if not ok:
        return redirect(url_for("backup_page"))
    try:
        if os.path.exists(DATABASE):
            cur = sqlite3.connect(DATABASE)
            saf = sqlite3.connect(DATABASE + ".safety")
            cur.backup(saf)
            saf.close()
            cur.close()
    except Exception:
        pass
    db = g.pop("db", None)
    if db is not None:
        db.close()
    with open(DATABASE, "wb") as fh:
        fh.write(raw)
    init_db()
    return redirect(url_for("home"))


@app.route("/footer-text", methods=["POST"])
@login_required
def footer_text_save():
    _set_setting("footer_text",
                 request.form.get("footer_text", "").strip())
    return redirect(request.referrer or url_for("home"))


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        if not is_admin():
            return redirect(url_for("login", next=request.path))
        _set_setting("about_text",
                     request.form.get("about_text", "").strip())
        return redirect(url_for("about"))
    html = BASE_HEAD + """
<h2>About Us / Kan Khrihfabu Kong</h2>
<div class="card"><div style="white-space:pre-line;font-size:17px;line-height:1.75">{{ about_text }}</div></div>
<div class="card"><h3>Connect With Us</h3>
<p>Khrihfabu thawng le pumhnak video pawl cu kan Facebook le Instagram ah zoh khawh a si.</p>
{% if social.facebook or social.instagram %}<div class="social-btns">
{% if social.facebook %}<a class="social-btn fb" href="{{ social.facebook }}" target="_blank" rel="noopener">Facebook</a>{% endif %}
{% if social.instagram %}<a class="social-btn ig" href="{{ social.instagram }}" target="_blank" rel="noopener">Instagram</a>{% endif %}
</div>{% else %}<p class="empty">Link a um rih lo.</p>{% endif %}
{% if is_admin %}<details class="edit-box"><summary>Link Edit / Remh</summary>
<form method="post" action="/about/social">
<label>Facebook Page URL</label>
<input name="facebook_url" type="url" placeholder="https://www.facebook.com/..." value="{{ social.facebook }}">
<label>Instagram URL</label>
<input name="instagram_url" type="url" placeholder="https://www.instagram.com/..." value="{{ social.instagram }}">
<button class="btn" type="submit">Save / Fim</button></form></details>{% endif %}
</div>
<div class="card" id="contact"><h3>Contact Us / Kan Sin Ah Thawng Kuat</h3>
{% if sent == "1" %}<p class="ok-note">Kan lawm tuk — na thawng a phan cang. A rang khawh chungin kan in leh lai.</p>{% endif %}
{% if sent == "0" %}<p class="err-note">A kal lo — na tial mi check ṭhan law a tanglei in kuat ṭhan tuah.</p>{% endif %}
{% if contact_on %}<p>Thawng a si ah, thlacam cah na duh mi (prayer request) a si ah — a tanglei form in kuat khawh a si. Na email le phone cu kan in lehnak ding lawngah kan hmang lai.</p>
<form method="post" action="/contact">
<label>Na Min / Your Name *</label>
<input name="name" required maxlength="80">
<label>Na Email *</label>
<input name="email" type="email" required maxlength="120">
<label>Phone Nambar / Phone</label>
<input name="phone" maxlength="40">
<label>Topic</label>
<select name="topic"><option value="Message">Message / Thawng</option><option value="Prayer Request">Prayer Request / Thlacam Sawnh</option></select>
<label>Na Thawng / Message *</label>
<textarea name="message" rows="6" required maxlength="4000" placeholder="Na duh mi thawng silole thlacam sawnh hika hin tial..."></textarea>
<input name="website" style="display:none" tabindex="-1" autocomplete="off">
<button class="btn" type="submit">Kuat / Send</button></form>
{% elif is_admin %}<p class="empty">Admin theih ding: contact form hi rian a ṭuan rih lo — Render Environment ah RCBC_CONTACT_TO, RCBC_SMTP_USER, RCBC_SMTP_PASS (Gmail App Password) chiah a hau rih.</p>{% endif %}
</div>
{% if is_admin %}<div class="card"><h3>About Edit / Church Information Edit</h3>
<form method="post">
<label>Church Information / Khrihfabu kong tialnak</label>
<textarea name="about_text" rows="10" class="auto-grow">{{ about_text }}</textarea>
<button class="btn" type="submit">Save</button></form></div>{% endif %}
""" + BASE_FOOT
    return render_template_string(
        html, title="About Us", active="about", church=CHURCH,
        about_text=get_about_text(),
        social=get_social_links(),
        contact_on=contact_config()["on"],
        sent=request.args.get("sent", ""),
    )



SCRIPTURES_HTML = """
<h2>Pathian Bia / Thawngtha Bia</h2>
{% if scriptures %}{% for sc in scriptures %}
<div class="card"><h3>{{ sc.title }}</h3>
{% if sc.date %}<p><small>{{ sc.date }}</small></p>{% endif %}
<div class="scripture-body">{{ sc.body }}</div>
{% if is_admin %}<div class="leader-actions"><a href="/pathian-bia/edit/{{ sc.id }}">Edit</a>
<form method="post" action="/pathian-bia/delete/{{ sc.id }}" onsubmit="return confirm('Hi Pathian bia hi delete duh taktak maw?')"><button type="submit">Delete</button></form></div>
<details class="edit-box"><summary>Edit / Remh (hitta zong)</summary>
<form method="post" action="/pathian-bia/edit/{{ sc.id }}">
<label>Title / Lu *</label><input name="title" required value="{{ sc.title }}">
<label>Date / Ni</label><input name="date" type="date" value="{{ sc.date }}">
<label>Cabia / Pathian Bia</label>
<textarea name="body" class="auto-expand" rows="8">{{ sc.body }}</textarea>
<button class="btn" type="submit">Save / Fim</button></form></details>{% endif %}
</div>{% endfor %}
{% else %}<div class="card"><p class="empty">Pathian bia a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p></div>{% endif %}
{% if is_admin %}<div class="card"><h3>Pathian Bia Thar Chiah / Add Scripture</h3>
<p class="empty">Pathian bia tial na duh ah cun ka hin Title tial law, Cabia box
ngan ah Pathian bia na duhmi tial; na tial pah ah box cu amah tein expand aa tuah lai (auto-expand).</p>
<form method="post">
<label>Title / Tlangtar *</label>
<input name="title" required placeholder="e.g. Zumhnak in kan kal - 2 Korin 5:7">
<label>Date / Ni</label>
<input name="date" type="date" value="{{ today }}">
<label>Cabia / Pathian Bia</label>
<textarea name="body" class="auto-expand" rows="10" placeholder="Pathian bia na duhmi hika hin tial..."></textarea>
<button class="btn" type="submit">Add Scripture / Pathian Bia Chiah</button>
</form></div>{% endif %}
"""

SCRIPTURE_EDIT_HTML = """
<h2>Edit Scripture / Pathian Bia Remh</h2>
<div class="card"><form method="post">
<label>Title / Tlangtar *</label>
<input name="title" required value="{{ sc.title }}">
<label>Date / Ni</label>
<input name="date" type="date" value="{{ sc.date }}">
<label>Cabia / Pathian Bia</label>
<textarea name="body" class="auto-expand" rows="10">{{ sc.body }}</textarea>
<button class="btn" type="submit">Save / Fim</button>
<a href="/pathian-bia">Cancel / Kir Than</a>
</form></div>
"""


@app.route("/pathian-bia", methods=["GET", "POST"])
def pathian_bia():
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            sc_date = request.form.get("date", "").strip() \
                or date.today().isoformat()
            sql = "INSERT INTO scriptures (title, body, date) VALUES (?,?,?)"
            params = (title, request.form.get("body", "").strip(), sc_date)
            try:
                db.execute(sql, params)
                db.commit()
            except sqlite3.OperationalError:
                init_db()
                db.execute(sql, params)
                db.commit()
        return redirect(url_for("pathian_bia"))
    html = BASE_HEAD + SCRIPTURES_HTML + BASE_FOOT
    return render_template_string(
        html, title="Pathian Bia", active="scripture", church=CHURCH,
        scriptures=get_scriptures(), today=date.today().isoformat())


@app.route("/pathian-bia/edit/<int:sc_id>", methods=["GET", "POST"])
@login_required
def edit_scripture(sc_id):
    db = get_db()
    try:
        row = db.execute("SELECT * FROM scriptures WHERE id=?",
                         (sc_id,)).fetchone()
    except sqlite3.OperationalError:
        init_db()
        row = db.execute("SELECT * FROM scriptures WHERE id=?",
                         (sc_id,)).fetchone()
    if row is None:
        return redirect(url_for("pathian_bia"))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            db.execute(
                "UPDATE scriptures SET title=?, body=?, date=? WHERE id=?",
                (title, request.form.get("body", "").strip(),
                 request.form.get("date", "").strip(), sc_id))
            db.commit()
        return redirect(url_for("pathian_bia"))
    html = BASE_HEAD + SCRIPTURE_EDIT_HTML + BASE_FOOT
    return render_template_string(
        html, title="Edit Scripture", active="scripture", church=CHURCH,
        sc=dict(row))


@app.route("/pathian-bia/delete/<int:sc_id>", methods=["POST"])
@login_required
def delete_scripture(sc_id):
    db = get_db()
    try:
        db.execute("DELETE FROM scriptures WHERE id=?", (sc_id,))
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.execute("DELETE FROM scriptures WHERE id=?", (sc_id,))
        db.commit()
    return redirect(url_for("pathian_bia"))


CAAN_HTML = """
<h2>Caan Ngeitu / Service Duty Roster</h2>
<div class="card"><h3>Pumhnak Caan / Service Times</h3>
<p><strong>Friday Zan Pumhnak:</strong> {{ times.friday_time }}<br>
<strong>Sunday Pumhnak:</strong> {{ times.sunday_time }}</p>
{% if is_admin %}<details class="edit-box"><summary>Caan Thlen / Edit Times</summary>
<form method="post" action="/service-times">
<label>Friday Pumhnak Caan / Friday Service Time</label>
<input name="friday_time" value="{{ times.friday_time }}" placeholder="e.g. 7:00 PM">
<label>Sunday Pumhnak Caan / Sunday Service Time</label>
<input name="sunday_time" value="{{ times.sunday_time }}" placeholder="e.g. 1:00 PM - 3:00 PM">
<input type="hidden" name="next" value="/caan-ngeitu">
<button class="btn" type="submit">Save Times / Caan Fim</button>
</form></details>{% endif %}</div>

<datalist id="duty-roles">{% for r in duty_roles %}<option value="{{ r }}">{% endfor %}</datalist>
{% if services %}{% for sv in services %}
<div class="card">
<div class="duty-head"><h3>{{ sv.service_date }}{% if sv.title %} - {{ sv.title }}{% endif %}{% if sv.service_time %} &middot; {{ sv.service_time }}{% endif %}</h3></div>
{% if sv['items'] %}<table class="duty-table">
{% for it in sv['items'] %}<tr><td>{{ it.role }}</td><td>{{ it.person }}</td></tr>{% endfor %}
</table>{% else %}<p class="empty">Hi pumhnak ah rian tlar a um rih lo.</p>{% endif %}
{% if sv.note %}<p style="white-space:pre-line">{{ sv.note }}</p>{% endif %}
{% if is_admin %}<div class="leader-actions"><a href="/caan-ngeitu/edit/{{ sv.id }}">Edit</a>
<form method="post" action="/caan-ngeitu/delete/{{ sv.id }}" onsubmit="return confirm('Hi pumhnak hi delete duh taktak maw?')"><button type="submit">Delete</button></form></div>
<details class="edit-box" open><summary>Quick Edit - Min Thlen Colh / Edit Names &amp; Save</summary>
<form method="post" action="/caan-ngeitu/edit/{{ sv.id }}">
<label>Date / Ni *</label><input name="service_date" type="date" value="{{ sv.service_date }}" required>
<label>Title / Pumhnak Lu *</label><input name="title" required value="{{ sv.title }}" placeholder="e.g. Sunday Pumhnak / Friday zan Pumhnak">
<label>Pumhnak Phun / Service Type</label>
<select name="service_type"><option value="">-- Thim / Choose --</option><option value="friday" {% if sv.service_type=='friday' %}selected{% endif %}>Friday Zan - {{ times.friday_time }}</option><option value="sunday" {% if sv.service_type=='sunday' %}selected{% endif %}>Sunday - {{ times.sunday_time }}</option><option value="other" {% if sv.service_type=='other' %}selected{% endif %}>Other</option></select>

<label>Rian le A Ngeitu / Duty Rows</label>
<div class="duty-rows">{% for it in sv['items'] %}<div class="duty-row">
<input name="role" list="duty-roles" placeholder="Rian - e.g. Pumh Hruaitu" value="{{ it.role }}">
<input name="person" placeholder="A Ngeitu - e.g. Upa Min" value="{{ it.person }}">
<button type="button" class="remove-duty-row">Hloh</button></div>{% endfor %}
{% if not sv['items'] %}<div class="duty-row">
<input name="role" list="duty-roles" placeholder="Rian - e.g. Pumh Hruaitu">
<input name="person" placeholder="A Ngeitu - e.g. Upa min">
<button type="button" class="remove-duty-row">Hloh</button></div>{% endif %}</div>
<button type="button" class="add-duty-row">+ Tlar Thar Chap / Add Row</button>
<label>Note</label><textarea name="note" rows="2">{{ sv.note }}</textarea>
<button class="btn" type="submit">Save / Fim</button></form></details>{% endif %}
</div>{% endfor %}
{% else %}<div class="card"><p class="empty">Caan ngeitu pumhnak a um rih lo.{% if is_admin %} A tanglei form in thar chiah khawh a si.{% endif %}</p></div>{% endif %}
{% if is_admin %}<div class="card"><h3>Pumhnak Thar Chiah / Add Service</h3>
<p class="empty">Code chungah tial hau lo - Date le Title thim law
(e.g. 2026-11-08, Sunday Pumhnak; 2026-11-06, Friday zan Pumhnak),
a tangah Rian le A Ngeitu tlar tial. Tlar tam deuh duh ah
"+ Tlar Thar Chap" hmet; rian cu pumhnak cio ningin a dang khawh.</p>
<p>Zarhkhat pumhnak pahnih: <strong>Friday zan {{ times.friday_time }}</strong> le
<strong>Sunday {{ times.sunday_time }}</strong>. A ra lai mi caah pakhat hmet:
<a href="/caan-ngeitu?stype=friday">Next Friday ({{ next_friday }})</a> &middot;
<a href="/caan-ngeitu?stype=sunday">Next Sunday ({{ next_sunday }})</a>
- date le title cu amah tein a lut lai.</p>
<form method="post">
<label>Date / Ni *</label>
<input name="service_date" type="date" value="{{ pre_date or today }}" required>
<label>Title / Pumhnak Lu *</label>
<input name="title" required value="{{ pre_title }}" placeholder="e.g. Sunday Pumhnak / Friday zan Pumhnak">
<label>Pumhnak Phun / Service Type</label>
<select name="service_type"><option value="">-- Thim / Choose --</option><option value="friday" {% if pre_type=='friday' %}selected{% endif %}>Friday Zan - {{ times.friday_time }}</option><option value="sunday" {% if pre_type=='sunday' %}selected{% endif %}>Sunday - {{ times.sunday_time }}</option><option value="other" {% if pre_type=='other' %}selected{% endif %}>Other</option></select>
<label>Rian le A Ngeitu / Duty Rows</label>
<div class="duty-rows">{% for i in range(5) %}<div class="duty-row">
<input name="role" list="duty-roles" placeholder="Rian - e.g. Pumh Hruaitu">
<input name="person" placeholder="A Ngeitu - e.g. Upa min">
<button type="button" class="remove-duty-row">Hloh</button></div>{% endfor %}</div>
<button type="button" class="add-duty-row">+ Tlar Thar Chap / Add Row</button>
<label>Note</label>
<textarea name="note" rows="2"></textarea>
<button class="btn" type="submit">Add Service / Pumhnak Chiah</button>
</form></div>{% endif %}
"""

CAAN_EDIT_HTML = """
<h2>Edit Service / Pumhnak Remh</h2>
<datalist id="duty-roles">{% for r in duty_roles %}<option value="{{ r }}">{% endfor %}</datalist>
<div class="card"><h3>{{ sv.service_date }}{% if sv.title %} - {{ sv.title }}{% endif %}</h3>
<form method="post">
<label>Date / Ni *</label>
<input name="service_date" type="date" value="{{ sv.service_date }}" required>
<label>Title / Pumhnak Lu *</label>
<input name="title" required value="{{ sv.title }}">
<label>Pumhnak Phun / Service Type</label>
<select name="service_type"><option value="">-- Thim / Choose --</option><option value="friday" {% if sv.service_type=='friday' %}selected{% endif %}>Friday Zan - {{ times.friday_time }}</option><option value="sunday" {% if sv.service_type=='sunday' %}selected{% endif %}>Sunday - {{ times.sunday_time }}</option><option value="other" {% if sv.service_type=='other' %}selected{% endif %}>Other</option></select>
<label>Rian le A Ngeitu / Duty Rows</label>
<div class="duty-rows">{% for it in items %}<div class="duty-row">
<input name="role" list="duty-roles" placeholder="Rian - e.g. Pumh Hruaitu" value="{{ it.role }}">
<input name="person" placeholder="A Ngeitu - e.g. Upa min" value="{{ it.person }}">
<button type="button" class="remove-duty-row">Hloh</button></div>{% endfor %}
<div class="duty-row">
<input name="role" list="duty-roles" placeholder="Rian - e.g. Pumh Hruaitu">
<input name="person" placeholder="A Ngeitu - e.g. Upa min">
<button type="button" class="remove-duty-row">Hloh</button></div></div>
<button type="button" class="add-duty-row">+ Tlar Thar Chap / Add Row</button>
<label>Note</label>
<textarea name="note" rows="2">{{ sv.note }}</textarea>
<button class="btn" type="submit">Save / Fim</button>
<a href="/caan-ngeitu">Cancel / Kir Than</a>
</form></div>
"""


@app.route("/caan-ngeitu", methods=["GET", "POST"])
def caan_ngeitu():
    db = get_db()
    if request.method == "POST" and not is_admin():
        return redirect(url_for("login", next=request.path))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        sdate = request.form.get("service_date", "").strip() \
            or date.today().isoformat()
        if title:
            stype = request.form.get("service_type", "").strip()
            if stype not in WEEKLY_SERVICES and stype != "other":
                stype = ""
            sql = ("INSERT INTO services "
                   "(service_date, service_type, title, note) "
                   "VALUES (?,?,?,?)")
            params = (sdate, stype, title,
                      request.form.get("note", "").strip())
            items = _service_form_items()
            try:
                cur = db.execute(sql, params)
                _save_service_items(db, cur.lastrowid, items)
                db.commit()
            except sqlite3.OperationalError:
                init_db()
                cur = db.execute(sql, params)
                _save_service_items(db, cur.lastrowid, items)
                db.commit()
        return redirect(url_for("caan_ngeitu"))
    stype = request.args.get("stype", "").strip()
    pre_date = pre_title = pre_type = ""
    if stype in WEEKLY_SERVICES:
        _ws = WEEKLY_SERVICES[stype]
        pre_date = next_service_date(_ws["weekday"]).isoformat()
        pre_title = _ws["label"]
        pre_type = stype
    html = BASE_HEAD + CAAN_HTML + BASE_FOOT
    return render_template_string(
        html, title="Caan Ngeitu", active="caan", church=CHURCH,
        services=get_services(), duty_roles=DUTY_ROLE_SUGGESTIONS,
        today=date.today().isoformat(),
        next_friday=next_service_date(4).isoformat(),
        next_sunday=next_service_date(6).isoformat(),
        pre_date=pre_date, pre_title=pre_title, pre_type=pre_type,
        times=get_service_times())


@app.route("/caan-ngeitu/edit/<int:service_id>", methods=["GET", "POST"])
@login_required
def edit_service(service_id):
    db = get_db()
    sql_s = "SELECT * FROM services WHERE id=?"
    try:
        row = db.execute(sql_s, (service_id,)).fetchone()
    except sqlite3.OperationalError:
        init_db()
        row = db.execute(sql_s, (service_id,)).fetchone()
    if row is None:
        return redirect(url_for("caan_ngeitu"))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            stype = request.form.get("service_type", "").strip()
            if stype not in WEEKLY_SERVICES and stype != "other":
                stype = row["service_type"] or ""
            db.execute(
                "UPDATE services SET service_date=?, title=?, note=?, "
                "service_type=? WHERE id=?",
                (request.form.get("service_date", "").strip()
                 or row["service_date"], title,
                 request.form.get("note", "").strip(), stype, service_id))
            _save_service_items(db, service_id, _service_form_items())
            db.commit()
        return redirect(url_for("caan_ngeitu"))
    items = [dict(x) for x in db.execute(
        "SELECT * FROM service_items WHERE service_id=? "
        "ORDER BY sort_order ASC, id ASC", (service_id,)).fetchall()]
    html = BASE_HEAD + CAAN_EDIT_HTML + BASE_FOOT
    return render_template_string(
        html, title="Edit Service", active="caan", church=CHURCH,
        sv=dict(row), items=items, duty_roles=DUTY_ROLE_SUGGESTIONS,
        times=get_service_times())


@app.route("/caan-ngeitu/delete/<int:service_id>", methods=["POST"])
@login_required
def delete_service(service_id):
    db = get_db()
    try:
        db.execute("DELETE FROM service_items WHERE service_id=?",
                   (service_id,))
        db.execute("DELETE FROM services WHERE id=?", (service_id,))
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.execute("DELETE FROM service_items WHERE service_id=?",
                   (service_id,))
        db.execute("DELETE FROM services WHERE id=?", (service_id,))
        db.commit()
    return redirect(url_for("caan_ngeitu"))




@app.route("/church-logo")
def church_logo():
    db = get_db()
    try:
        row = db.execute(
            "SELECT data, mimetype FROM site_assets WHERE key='logo'"
        ).fetchone()
    except sqlite3.OperationalError:
        init_db()
        row = db.execute(
            "SELECT data, mimetype FROM site_assets WHERE key='logo'"
        ).fetchone()
    if row is None or not row["data"]:
        return ("Not Found", 404)
    data = bytes(row["data"])
    mime = row["mimetype"] or _detect_image_mimetype(data) \
        or "application/octet-stream"
    return send_file(io.BytesIO(data), mimetype=mime)


@app.route("/church-logo/upload", methods=["POST"])
@login_required
def upload_church_logo():
    data, mime, _err = _read_leader_photo(request.files.get("photo"))
    if data is not None and not _err:
        db = get_db()
        db.execute("DELETE FROM settings WHERE key='logo_disabled'")
        sql = ("INSERT OR REPLACE INTO site_assets (key, data, mimetype) "
               "VALUES ('logo',?,?)")
        try:
            db.execute(sql, (data, mime))
            db.commit()
        except sqlite3.OperationalError:
            init_db()
            db.execute(sql, (data, mime))
            db.commit()
    return redirect(url_for("home"))


@app.route("/church-logo/delete", methods=["POST"])
@login_required
def delete_church_logo():
    db = get_db()
    try:
        db.execute("DELETE FROM site_assets WHERE key='logo'")
        db.execute(
            "INSERT OR REPLACE INTO settings (key, value) "
            "VALUES ('logo_disabled','1')")
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.execute("DELETE FROM site_assets WHERE key='logo'")
        db.execute(
            "INSERT OR REPLACE INTO settings (key, value) "
            "VALUES ('logo_disabled','1')")
        db.commit()
    return redirect(url_for("home"))


@app.route("/service-times", methods=["POST"])
@login_required
def save_service_times():
    db = get_db()
    friday = request.form.get("friday_time", "").strip() \
        or DEFAULT_SERVICE_TIMES["friday_time"]
    sunday = request.form.get("sunday_time", "").strip() \
        or DEFAULT_SERVICE_TIMES["sunday_time"]
    sql = "INSERT OR REPLACE INTO settings (key, value) VALUES (?,?)"
    try:
        db.executemany(sql, [("friday_time", friday),
                             ("sunday_time", sunday)])
        db.commit()
    except sqlite3.OperationalError:
        init_db()
        db.executemany(sql, [("friday_time", friday),
                             ("sunday_time", sunday)])
        db.commit()
    nxt = request.form.get("next", "").strip()
    if nxt.startswith("/"):
        return redirect(nxt)
    return redirect(url_for("caan_ngeitu"))


if __name__ == "__main__":
    init_db()
    print("Raleigh Chin Baptist Church website: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
