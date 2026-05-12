from pathlib import Path
root = Path('/tmp/qcm-publish')
source = root / 'qcm-police-procedure-penale.html'
target = root / 'index.html'
content = source.read_text(encoding='utf-8')
content = content.replace('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n', '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#1a3a6b">\n<meta name="description" content="Application web de revision police, installable sur iPhone depuis Safari.">\n', 1)
content = content.replace('<meta name="apple-mobile-web-app-status-bar-style" content="default">\n', '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n<meta name="apple-mobile-web-app-title" content="QCM Police">\n<link rel="manifest" href="./manifest.webmanifest">\n<link rel="icon" href="./icon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="./icon.svg">\n', 1)
content = content.replace('.header p { font-size: 13px; opacity: 0.75; margin-top: 4px; }\n', '.header p { font-size: 13px; opacity: 0.75; margin-top: 4px; }\n.install-note { margin-top: 10px; padding: 10px 12px; border-radius: 10px; background: rgba(255,255,255,0.12); font-size: 12px; line-height: 1.5; }\n.install-note strong { color: #fff; }\n', 1)
content = content.replace('    <p>Entraînement aux cadres juridiques et procédures</p>\n', '    <p>Entraînement aux cadres juridiques et procédures</p>\n    <p class="install-note"><strong>iPhone :</strong> ouvrez ce site dans Safari, touchez <strong>Partager</strong>, puis <strong>Sur l\'ecran d\'accueil</strong>.</p>\n', 1)
content = content.replace('buildSubjectMenu();\n', 'buildSubjectMenu();\n\nif ("serviceWorker" in navigator) {\n  window.addEventListener("load", () => {\n    navigator.serviceWorker.register("./service-worker.js").catch((error) => {\n      console.error("Service worker non enregistre", error);\n    });\n  });\n}\n', 1)
target.write_text(content, encoding='utf-8')
print(f"Web app mise a jour: {target}")
