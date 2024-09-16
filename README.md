## Introduction

- 本アプリケーションはオンライン英会話学習者向けの学習補助アプリケーションとなります。
  - 本リポジトリはBackendのコードを格納しております。
  - [Frontend](https://github.com/bigface0202/english-learning-feedback-frontend)は別リポジトリに格納しています。
- 機能としては以下を搭載しております。
  - 録音された音声データから話者を認識した文字起こし
  - 文字起こしデータを利用したボキャブラリーの可視化
  - 会話内容の改善点の提案
- [AI Hackathon with Google Cloud](https://googlecloudjapanaihackathon.devpost.com/)向けに作られたアプリケーションです。

## Architecture

![Architecture](data/english-learning-feedback.png)

## Tech Stack

- Python
- Vue.js
- Cloud Run
- Cloud Storage
- Vertex AI(Gemini)
- Firebase
- Firestore

## TODO

- [x] Check SpeechToText
- [x] Check VertexAI Gemini
- [x] Check VertexAI Gemini with system instructions
- [ ] Check LangChain Gemini
- [x] High-level architecture
- [x] Check Gemini opearation as REST API
- [x] Implement recording and uploading audio file through Flutter

### Backend

- [x] Gemini text service
- [x] Gemini audio service
- [x] Text parse function
- [x] Analyze text data
- [x] Storing DB
