import streamlit as st
import random

# ---------------------------------------------------------
# Streamlitページの基本設定
# ---------------------------------------------------------
st.set_page_config(
    page_title="和風おみくじアプリ",
    page_icon="🎋",
    layout="centered"
)

# ---------------------------------------------------------
# 和風デザイン用のCSS
# 背景色やカード風デザインを設定します
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fdf6f0 0%, #f7efe5 100%);
    }

    .main-title {
        text-align: center;
        color: #7a3b2e;
        font-size: 2.4rem;
        font-weight: bold;
        margin-bottom: 0.3rem;
    }

    .sub-text {
        text-align: center;
        color: #6b5b53;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    .fortune-card {
        background: #fffaf5;
        border: 2px solid #e7c9a9;
        border-radius: 20px;
        padding: 24px;
        margin-top: 20px;
        box-shadow: 0 8px 20px rgba(122, 59, 46, 0.12);
    }

    .fortune-rank {
        font-size: 2rem;
        font-weight: bold;
        color: #b04a3a;
        text-align: center;
        margin-bottom: 10px;
    }

    .fortune-message {
        font-size: 1.1rem;
        color: #4f403b;
        line-height: 1.8;
        margin-bottom: 18px;
        text-align: center;
    }

    .fortune-detail {
        background: #fff;
        border-radius: 14px;
        padding: 12px 16px;
        margin: 8px 0;
        border: 1px solid #f0d8bf;
        color: #5a4a42;
        font-size: 1rem;
    }

    .beginner-box {
        background: #fef3e8;
        border-left: 6px solid #d98c5f;
        padding: 14px 16px;
        border-radius: 10px;
        color: #5c4b43;
        margin-top: 18px;
    }

    div.stButton > button {
        background-color: #c86b4a;
        color: white;
        border-radius: 999px;
        border: none;
        padding: 0.7rem 1.4rem;
        font-size: 1.05rem;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #a95438;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# おみくじデータ
# 各運勢ごとに、表示する内容を辞書でまとめています
# ---------------------------------------------------------
omikuji_data = [
    {
        "rank": "大吉 ✨",
        "message": "今日は最高の運気です。新しいことに挑戦すると、大きなチャンスにつながりそうです。",
        "lucky_color": "金色",
        "lucky_number": 8,
        "lucky_item": "お守り"
    },
    {
        "rank": "中吉 🌟",
        "message": "とても良い日です。落ち着いて行動すると、うれしい結果がついてきます。",
        "lucky_color": "えんじ色",
        "lucky_number": 6,
        "lucky_item": "和柄のハンカチ"
    },
    {
        "rank": "吉 🍀",
        "message": "幸運がじわじわと近づいています。人との会話を大切にすると運気アップです。",
        "lucky_color": "若草色",
        "lucky_number": 3,
        "lucky_item": "小さなノート"
    },
    {
        "rank": "小吉 😊",
        "message": "穏やかな一日になりそうです。あせらず、自分のペースで進むことが大切です。",
        "lucky_color": "桜色",
        "lucky_number": 2,
        "lucky_item": "温かいお茶"
    },
    {
        "rank": "凶 ⚠️",
        "message": "今日は無理をせず、休息を意識して過ごしましょう。ていねいな行動が運気回復の鍵です。",
        "lucky_color": "藍色",
        "lucky_number": 9,
        "lucky_item": "お気に入りの本"
    }
]

def draw_omikuji():
    """ランダムでおみくじ結果を1つ選んで返す関数"""
    return random.choice(omikuji_data)

# ---------------------------------------------------------
# アプリのタイトル表示
# ---------------------------------------------------------
st.markdown('<div class="main-title">🎋 和風おみくじアプリ 🎋</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">ボタンを押して、今日の運勢を楽しく占ってみましょう😊</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 「おみくじを引く」ボタン
# ※元のボタンは残しています
# ---------------------------------------------------------
if st.button("✨ おみくじを引く ✨"):
    # おみくじを引く
    result = draw_omikuji()

    # 風船の演出はそのまま残します
    st.balloons()

    # 見出し表示
    st.subheader("🎉 あなたのおみくじの結果は… 🎉")

    # 結果をカード風に表示
    st.markdown(
        f"""
        <div class="fortune-card">
            <div class="fortune-rank">{result["rank"]}</div>
            <div class="fortune-message">{result["message"]}</div>
            <div class="fortune-detail">🎨 <b>ラッキーカラー：</b> {result["lucky_color"]}</div>
            <div class="fortune-detail">🔢 <b>ラッキーナンバー：</b> {result["lucky_number"]}</div>
            <div class="fortune-detail">🎁 <b>ラッキーアイテム：</b> {result["lucky_item"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 初心者向けコメント
    st.markdown(
        """
        <div class="beginner-box">
            💡 <b>初心者向けコメント</b><br>
            Streamlitでは、<code>st.button()</code>でボタンを作り、
            押されたときに処理を実行できます。<br>
            また、<code>st.markdown()</code>にHTMLやCSSを組み合わせることで、
            このようなおしゃれなデザインも作れます。
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # 初期状態で表示する案内
    st.info("「✨ おみくじを引く ✨」ボタンを押すと、今日の運勢が表示されます。")
