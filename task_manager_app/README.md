# Task Manager App

## 📘 概要
このアプリは、**Django** を使用して作成したシンプルなタスク管理アプリです。  
「自分のタスクを簡単に可視化して進捗管理したい」という目的で開発しました。

---

## 🚀 主な機能
- ✅ タスクの一覧表示  
- ➕ タスクの追加（タイトル・説明・締切日）  
- ✏️ タスクの編集  
- ❌ タスクの削除  
- 📊 進捗（progress）と完了フラグの管理

---

## 🛠 使用技術
- **言語**：Python 3.14  
- **フレームワーク**：Django 5.2  
- **データベース**：SQLite3  
- **テンプレート**：HTML + Django Template Language  
- **環境**：Mac（M1）

---

## 🖥 画面構成
| ページ | URL | 内容 |
|--------|------|------|
| タスク一覧 | `/tasks/` | 登録されたタスクを表示 |
| タスク追加 | `/tasks/add/` | 新しいタスクを追加 |
| タスク編集 | `/tasks/edit/<id>/` | 既存タスクを編集 |
| タスク削除 | `/tasks/delete/<id>/` | タスクを削除 |

---

## ⚙️ ローカル実行方法（再現手順）

```bash
# 仮想環境を作成して有効化
python3 -m venv venv
source venv/bin/activate

# 必要なパッケージをインストール
pip install django

# マイグレーション実行
python3 manage.py makemigrations
python3 manage.py migrate

# サーバー起動
python3 manage.py runserver
