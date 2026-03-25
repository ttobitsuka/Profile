import streamlit as st

# ページ設定（スマホで見やすい幅にする）
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
    line_url = "https://line.me/ti/p/YOUR_ID_HERE" 
    
    if st.button("🟢 LINEでつながる"):
        st.markdown(f'<a href="{line_url}" target="_blank">ここをタップしてLINEを開く</a>', unsafe_allow_html=True)
    
    st.caption("※QRコードをスクショしてここに貼るのもアリです")

# --- 応援歌エディタへのリンク（自作アプリの宣伝） ---
st.divider()
st.write("👇 最近作ったアプリ")
if st.button("🎺 応援歌エディタを開く"):
    st.write("（ここに自分のアプリのURLをリンクさせる）")
