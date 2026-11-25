# Lab 8 – Step-by-step (macOS Terminal)

Image names required by the lab (username = `ces13`, name = `Chelsey_Saydi`):

| Image | Port | Tag |
|---|---|---|
| Lab 5 Postman & APIs app | 5000 | `ces13/lab8-chelsey_saydi:0.0.1.RELEASE` |
| `GET /get_users` app | 3000 | `ces13/lab8-chelsey_saydi:0.0.2.RELEASE` |

Make sure **Docker Desktop is open and running** before starting.
Open Terminal and run:  `cd ~/Lab8`

---

## Part A – Build & run image 1 (port 5000)

```bash
cd lab8-image1
docker image build -t ces13/lab8-chelsey_saydi:0.0.1.RELEASE .
docker run -p 5000:5000 -d --name lab8_api_v1 ces13/lab8-chelsey_saydi:0.0.1.RELEASE
```

Test it (browser or Postman): <http://localhost:5000/api/users>  → returns John Doe.
Call it 2–3 times so there are request lines in the logs.

## Part B – Activity 1 commands (take a screenshot after EACH one)

```bash
docker ps -a                 # screenshot 1
docker stop lab8_api_v1      # screenshot 2  (also run `docker ps -a` again to show "Exited")
docker logs lab8_api_v1      # screenshot 3
```

Paste the three screenshots into **Lab8_Activity1_Chelsey_Saydi.docx** in the yellow boxes, then delete the boxes.

> The lab writes `docker stop <image_name>`, but the argument is really the **container** name/ID
> (`lab8_api_v1`, or the CONTAINER ID shown by `docker ps -a`). This is explained in the Word doc.

## Part C – Build & run image 2 (port 3000)

```bash
docker start lab8_api_v1     # restart image-1 container so both show "In use"
cd ../lab8-image2
docker image build -t ces13/lab8-chelsey_saydi:0.0.2.RELEASE .
docker run -p 3000:3000 -d --name lab8_api_v2 ces13/lab8-chelsey_saydi:0.0.2.RELEASE
```

Test it: <http://localhost:3000/get_users>  → `["John Doe"]`

## Part D – Activity 2 screenshots

1. Open **Docker Desktop → Images (Local tab)**. Take a screenshot showing both
   `ces13/lab8-chelsey_saydi` rows with tags `0.0.1.RELEASE` and `0.0.2.RELEASE`
   and status **In use** (same as the screenshot in the lab PDF).
2. Optional but recommended: screenshot of `docker images` in Terminal, and of the
   two endpoints working in the browser / Postman (`/api/users` on 5000, `/get_users` on 3000).

## Cleanup (only after you have all screenshots)

```bash
docker stop lab8_api_v1 lab8_api_v2
docker rm   lab8_api_v1 lab8_api_v2
```

---

## Troubleshooting

* **"port is already allocated"** – something else is on 5000/3000. Stop it, or change the host
  port, e.g. `-p 5001:5000` (the second number must stay the same).
* **Page doesn't load / connection refused** – the app must listen on `0.0.0.0`
  (already set in both `app.py` files with `app.run(host="0.0.0.0", port=...)`).
* **`docker: command not found`** – Docker Desktop isn't running, open it and wait for the whale icon, then retry.
* **Build fails installing Flask** – the lab's `python:3.8-alpine` is too old for `flask==3.1.3`;
  the Dockerfiles already use `python:3.11-alpine`.

> Docker image names must be lowercase, so the tag is `ces13/lab8-chelsey_saydi` (same as the instructor's `imangh84/lab8-imanghalayini`).
> Mac screenshot shortcut: **Cmd+Shift+4** then drag over the Terminal / Docker Desktop window.
