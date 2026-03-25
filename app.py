import streamlit as st
from PIL import Image # 画像を扱うためのライブラリ

# 1. ページ設定
st.set_page_config(page_title="My Digital Profile", layout="centered")

# --- カスタムCSS（デザインをかっこよくする） ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #00B900; /* LINEカラー */
        color: white;
        font-weight: bold;
        border: none;
    }
    .profile-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- プロフィール表示 ---
st.markdown('<div class="profile-card">', unsafe_allow_html=True)
st.title("⚾️ My Profile")
st.write("Procurement Specialist / AI Developer / Baseball Player")
st.markdown('</div>', unsafe_allow_html=True)

# --- コンテンツ（タブで切り替え） ---
tab1, tab2, tab3 = st.tabs(["About Me", "Skills", "Contact"])

with tab1:
    st.subheader("自己紹介")
    st.write("スズキ株式会社で購買の仕事をしながら、個人でAIアプリ開発やNoteでの執筆をしています。")
    st.info("趣味：野球（球速アップ挑戦中！）、筋トレ、応援歌作成")

with tab2:
    st.subheader("開発・スキル")
    col1, col2 = st.columns(2)
    with col1:
        st.write("✅ **IT/AI**")
        st.caption("Deep Learning / Streamlit")
    with col2:
        st.write("✅ **Sports**")
        st.caption("Baseball Data Analysis")

with tab3:
    st.subheader("Let's Connect!")
    st.write("お気軽にLINE追加してください！")
    
    # LINEのURL（自分のQRコードのURLをここに入れる）
    # line_url = "https://line.me/ti/p/YOUR_ID_HERE" 
    
    # --- 【ここが追加部分！】 ---
    try:
        # ステップ2でアップロードした画像を読み込む
        qr_image = Image.open("line-qr.png")
        
        # 画像を表示（width=200 で大きさを調整）
        st.image(qr_image, caption="My LINE QR Code", width=200)
        
        st.success("👆 スマホのカメラで読み取ってください")
        
    except FileNotFoundError:
        # 画像がない場合の予備表示
        st.warning("⚠️ QRコード画像（line-qr.png）がGitHubに見つかりません。")
        st.info("ステップ2の手順で画像をアップロードしてください。")
    # --------------------------

# --- 応援歌エディタへのリンク ---
st.divider()
st.write("👇 最近作ったアプリ")
if st.button("🎺 応援歌エディタを開く"):
    # ここに自分の応援歌アプリのURLをリンクさせる
    st.write("（アプリのURLをここに貼ってください）")
