import streamlit as st
import random
import time
import requests

# ---------------------------------------------------------
# Streamlitページの基本設定
# ---------------------------------------------------------
st.set_page_config(
    page_title="和風おみくじアプリ Version5",
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

    @keyframes gentleGoldGlow {
        0% {
            box-shadow:
                0 0 0 4px rgba(255, 245, 180, 0.45),
                0 10px 28px rgba(212, 175, 55, 0.24),
                0 0 10px rgba(255, 224, 130, 0.18);
        }
        50% {
            box-shadow:
                0 0 0 5px rgba(255, 245, 180, 0.6),
                0 14px 34px rgba(212, 175, 55, 0.34),
                0 0 24px rgba(255, 224, 130, 0.34);
        }
        100% {
            box-shadow:
                0 0 0 4px rgba(255, 245, 180, 0.45),
                0 10px 28px rgba(212, 175, 55, 0.24),
                0 0 10px rgba(255, 224, 130, 0.18);
        }
    }

    @keyframes sparkleTwinkle {
        0% {
            opacity: 0.45;
            transform: scale(0.98);
            text-shadow: 0 0 4px rgba(255, 232, 150, 0.18);
        }
        50% {
            opacity: 1;
            transform: scale(1.03);
            text-shadow: 0 0 12px rgba(255, 215, 64, 0.34);
        }
        100% {
            opacity: 0.5;
            transform: scale(0.99);
            text-shadow: 0 0 4px rgba(255, 232, 150, 0.18);
        }
    }

    @keyframes rankShine {
        0% {
            text-shadow:
                1px 1px 0 #fff7cc,
                0 0 6px rgba(255, 215, 64, 0.16);
        }
        50% {
            text-shadow:
                1px 1px 0 #fff7cc,
                0 0 16px rgba(255, 215, 64, 0.38);
        }
        100% {
            text-shadow:
                1px 1px 0 #fff7cc,
                0 0 6px rgba(255, 215, 64, 0.16);
        }
    }

    .super-fortune-card {
        background: linear-gradient(135deg, #fffdf1 0%, #fff4be 35%, #ffe082 70%, #ffd54f 100%);
        border: 4px solid #d4af37;
        border-radius: 24px;
        padding: 28px;
        margin-top: 20px;
        position: relative;
        overflow: hidden;
        animation: gentleGoldGlow 3.2s ease-in-out infinite;
    }

    .super-fortune-card::before {
        content: "✦ ✨ ✦ ✨ ✦";
        position: absolute;
        top: 12px;
        right: 18px;
        font-size: 1.15rem;
        color: #c99700;
        letter-spacing: 2px;
        animation: sparkleTwinkle 2.8s ease-in-out infinite;
    }

    .super-fortune-card::after {
        content: "✨ ✦ ✨ ✦ ✨";
        position: absolute;
        bottom: 12px;
        left: 18px;
        font-size: 1.05rem;
        color: #c99700;
        letter-spacing: 2px;
        animation: sparkleTwinkle 3s ease-in-out infinite 0.7s;
    }

    .super-badge {
        display: inline-block;
        background: linear-gradient(90deg, #fff7cc 0%, #ffe082 100%);
        color: #8a5a00;
        font-weight: bold;
        border: 2px solid #d4af37;
        border-radius: 999px;
        padding: 8px 18px;
        margin: 0 auto 16px auto;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.22);
    }

    .super-badge-wrap {
        text-align: center;
    }

    .fortune-rank {
        font-size: 2rem;
        font-weight: bold;
        color: #b04a3a;
        text-align: center;
        margin-bottom: 10px;
    }

    .super-fortune-rank {
        font-size: 2.75rem;
        font-weight: bold;
        color: #9c6b00;
        text-align: center;
        margin-bottom: 12px;
        letter-spacing: 1px;
        animation: rankShine 2.8s ease-in-out infinite;
    }

    .fortune-message {
        font-size: 1.1rem;
        color: #4f403b;
        line-height: 1.8;
        margin-bottom: 18px;
        text-align: center;
    }

    .super-fortune-message {
        font-size: 1.14rem;
        color: #5f4700;
        line-height: 1.9;
        margin-bottom: 18px;
        text-align: center;
        font-weight: 600;
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

    .super-fortune-detail {
        background: rgba(255, 255, 255, 0.86);
        border-radius: 14px;
        padding: 12px 16px;
        margin: 8px 0;
        border: 1px solid #e6c55a;
        color: #5f4700;
        font-size: 1rem;
        font-weight: 600;
    }

    .score-title {
        margin-top: 18px;
        margin-bottom: 8px;
        font-size: 1.05rem;
        font-weight: bold;
        color: #8b5e3c;
    }

    .score-box {
        background: #fff8f1;
        border-radius: 14px;
        padding: 14px 16px;
        border: 1px solid #edd6be;
        color: #5a4a42;
        text-align: center;
    }

    .super-score-box {
        background: rgba(255, 250, 235, 0.9);
        border-radius: 14px;
        padding: 14px 16px;
        border: 1px solid #e6c55a;
        color: #5f4700;
        text-align: center;
    }

    .score-number {
        font-size: 2rem;
        font-weight: bold;
        color: #b04a3a;
        line-height: 1.4;
    }

    .super-score-number {
        font-size: 2.1rem;
        font-weight: bold;
        color: #9c6b00;
        line-height: 1.4;
    }

    .score-caption {
        font-size: 0.96rem;
        line-height: 1.7;
        margin-top: 4px;
    }

    .advice-title {
        margin-top: 18px;
        margin-bottom: 8px;
        font-size: 1.05rem;
        font-weight: bold;
        color: #8b5e3c;
    }

    .advice-text {
        background: #fff8f1;
        border-radius: 14px;
        padding: 12px 16px;
        border: 1px solid #edd6be;
        color: #5a4a42;
        font-size: 1rem;
        line-height: 1.8;
    }

    .super-advice-text {
        background: rgba(255, 250, 235, 0.9);
        border-radius: 14px;
        padding: 12px 16px;
        border: 1px solid #e6c55a;
        color: #5f4700;
        font-size: 1rem;
        line-height: 1.8;
        font-weight: 500;
    }

    .kotowaza-title {
        margin-top: 18px;
        margin-bottom: 8px;
        font-size: 1.05rem;
        font-weight: bold;
        color: #8b5e3c;
    }

    .kotowaza-box {
        background: #fff8f1;
        border-radius: 14px;
        padding: 14px 16px;
        border: 1px solid #edd6be;
        color: #5a4a42;
    }

    .super-kotowaza-box {
        background: rgba(255, 250, 235, 0.9);
        border-radius: 14px;
        padding: 14px 16px;
        border: 1px solid #e6c55a;
        color: #5f4700;
    }

    .kotowaza-quote {
        font-size: 1.15rem;
        font-weight: bold;
        margin-bottom: 8px;
        line-height: 1.8;
    }

    .kotowaza-description {
        font-size: 0.98rem;
        line-height: 1.8;
    }

    .jackpot-text {
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #9c6b00;
        margin-top: 12px;
        margin-bottom: 8px;
        text-shadow: 0 0 8px rgba(255, 215, 64, 0.25);
    }

    .countdown-box {
        text-align: center;
        color: #7a3b2e;
        font-weight: bold;
        margin-top: 18px;
        margin-bottom: 8px;
        min-height: 80px;
    }

    .countdown-text {
        font-size: 1.4rem;
        margin-bottom: 8px;
    }

    .countdown-number {
        font-size: 3rem;
        color: #c86b4a;
        line-height: 1.2;
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

    .mission-title{
        margin-top:20px;
        font-size:20px;
        font-weight:bold;
        color:#b85c38;
    }

    .mission-box{
        background:#fffaf5;
        border:1px solid #f0d6b8;
        border-radius:12px;
        padding:16px;
        margin-top:10px;
    }

    .mission-name{
        font-size:22px;
        font-weight:bold;
        color:#b85c38;
        margin-bottom:10px;
    }

    .mission-description{
        color:#666;
        line-height:1.8;
    }

    /* -------------------------------- */
    /* 結果カード ふわっと表示 */
    /* -------------------------------- */

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(25px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fortune-card,
    .super-fortune-card {
        animation: fadeInUp 0.8s ease-out;    }

    /* -------------------------------- */
    /* カウントダウン数字 ポンッ演出 */
    /* -------------------------------- */

    @keyframes countdownPop {
        0% {
            opacity: 0;
            transform: scale(0.2);
        }

        50% {
            opacity: 1;
            transform: scale(1.7);
        }

        70% {
            transform: scale(0.9);
        }

        85% {
            transform: scale(1.15);
        }

        100% {
            opacity: 1;
            transform: scale(1);
        }
    }

    .countdown-number {
        font-size: 64px;
        font-weight: bold;
        animation: countdownPop 0.45s ease-out;
    }

    /* -------------------------------- */
    /* 「結果が出ました！」演出 */
    /* -------------------------------- */

    @keyframes resultPop {
        0% {
            opacity: 0;
            transform: scale(0.4);
        }

        60% {
            opacity: 1;
            transform: scale(1.25);
        }

        80% {
            transform: scale(0.95);
        }

        100% {
            opacity: 1;
            transform: scale(1);
        }
    }

    .result-announcement {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        color: #b85c38;
        animation: resultPop 0.6s ease-out;
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
        "rank": "超大吉 👑",
        "message": "めったに出ない最高クラスの大幸運です。今日は思いきった挑戦や願いごとに追い風が吹く特別な一日になりそうです。",
        "lucky_color": "金色",
        "lucky_number": 1,
        "lucky_item": "きらめくアクセサリー",
        "advice": "自信をもって一歩踏み出してみましょう。感謝の気持ちを言葉にすると、さらに良いご縁が広がります。"
    },
    {
        "rank": "大吉 ✨",
        "message": "今日は最高の運気です。新しいことに挑戦すると、大きなチャンスにつながりそうです。",
        "lucky_color": "金色",
        "lucky_number": 8,
        "lucky_item": "お守り",
        "advice": "やってみたかったことを一つ行動に移してみてください。前向きな気持ちが運をぐっと引き寄せます。"
    },
    {
        "rank": "中吉 🌟",
        "message": "とても良い日です。落ち着いて行動すると、うれしい結果がついてきます。",
        "lucky_color": "えんじ色",
        "lucky_number": 6,
        "lucky_item": "和柄のハンカチ",
        "advice": "ていねいな確認を心がけると、物事がよりスムーズに進みます。小さな親切も開運のポイントです。"
    },
    {
        "rank": "吉 🍀",
        "message": "幸運がじわじわと近づいています。人との会話を大切にすると運気アップです。",
        "lucky_color": "若草色",
        "lucky_number": 3,
        "lucky_item": "小さなノート",
        "advice": "会話の中で思いついたことをメモしておきましょう。何気ないひらめきが良い流れを作ってくれます。"
    },
    {
        "rank": "小吉 😊",
        "message": "穏やかな一日になりそうです。あせらず、自分のペースで進むことが大切です。",
        "lucky_color": "桜色",
        "lucky_number": 2,
        "lucky_item": "温かいお茶",
        "advice": "少し深呼吸してから行動すると心が整います。無理をせず、できたことに目を向けてみてください。"
    },
    {
        "rank": "末吉 🌸",
        "message": "ゆっくりと運気が上向いていく日です。小さな幸せを見つけることで、気持ちも明るくなりそうです。",
        "lucky_color": "藤色",
        "lucky_number": 4,
        "lucky_item": "香りのよい文房具",
        "advice": "目の前の小さなことを丁寧にこなしてみましょう。積み重ねが次の幸運につながります。"
    },
    {
        "rank": "凶 ⚠️",
        "message": "今日は無理をせず、休息を意識して過ごしましょう。ていねいな行動が運気回復の鍵です。",
        "lucky_color": "藍色",
        "lucky_number": 9,
        "lucky_item": "お気に入りの本",
        "advice": "予定を詰め込みすぎず、ひとつずつ落ち着いて進めましょう。早めの休憩が気持ちの切り替えにつながります。"
    }
]

# ---------------------------------------------------------
# 今日のラッキーことわざ
# おみくじを引くたびに1つランダムで表示します
# ---------------------------------------------------------
kotowaza_list = [
    {
        "quote": "石の上にも三年",
        "description": "すぐに結果が出なくても、続けることが大切だという意味です。"
    },
    {
        "quote": "継続は力なり",
        "description": "小さな努力でも、続けることで大きな力になります。"
    },
    {
        "quote": "七転び八起き",
        "description": "失敗しても何度でも立ち上がれば大丈夫、という前向きな言葉です。"
    },
    {
        "quote": "塵も積もれば山となる",
        "description": "小さなことでも積み重ねれば、大きな成果につながります。"
    },
    {
        "quote": "急がば回れ",
        "description": "急いでいるときほど、落ち着いて確実な方法を選ぶのが大切です。"
    },
    {
        "quote": "笑う門には福来る",
        "description": "明るく笑顔でいると、よい運が集まりやすくなるという意味です。"
    },
    {
        "quote": "為せば成る",
        "description": "やろうと決めて努力すれば、道は開けるという励ましの言葉です。"
    },
    {
        "quote": "案ずるより産むが易し",
        "description": "心配しすぎるより、まずやってみると意外とうまくいくことがあります。"
    }
]

# ---------------------------------------------------------
# 今日の開運ミッション
# おみくじを引くたびに1つランダムで表示します
# ---------------------------------------------------------
mission_list = [
    {
        "mission": "😊 笑顔であいさつを3回してみよう",
        "description": "笑顔は幸運を呼び込む第一歩です。"
    },
    {
        "mission": "🧹 身の回りを1か所だけ整えよう",
        "description": "小さな整理が、気持ちと運気を整えてくれます。"
    },
    {
        "mission": "☕ いつもより少しゆっくり休憩しよう",
        "description": "心に余裕を作ることで、良い流れが生まれやすくなります。"
    },
    {
        "mission": "💬 誰かに感謝を伝えてみよう",
        "description": "感謝の言葉は、自分にも相手にも良い運気を届けます。"
    },
    {
        "mission": "🚶 5分だけ歩いて気分転換しよう",
        "description": "少し体を動かすことで、気持ちが前向きになります。"
    }
]

# ---------------------------------------------------------
# ラッキースコアの範囲設定
# 運勢ごとにランダムな点数範囲を変えます
# ---------------------------------------------------------
score_ranges = {
    "超大吉": (98, 100),
    "大吉": (90, 97),
    "吉": (75, 89),
    "中吉": (60, 74),
    "小吉": (45, 59),
    "末吉": (30, 44),
    "凶": (10, 29)
}

def draw_omikuji():
    """出現率を調整してランダムにおみくじ結果を返す関数"""
    weights = [2, 17, 18, 22, 18, 13, 10]  # 超大吉は約2%
    return random.choices(omikuji_data, weights=weights, k=1)[0]

def draw_kotowaza():
    """ランダムでことわざを1つ返す関数"""
    return random.choice(kotowaza_list)

def draw_mission():
    """ランダムで開運ミッションを1つ返す関数"""
    return random.choice(mission_list)

def get_lucky_score(rank):
    """運勢に応じたラッキースコアを返す関数"""
    for fortune_name, score_range in score_ranges.items():
        if fortune_name in rank:
            return random.randint(score_range[0], score_range[1])
    return random.randint(50, 80)

# ---------------------------------------------------------
# アプリのタイトル表示
# ---------------------------------------------------------
st.markdown('<div class="main-title">🎋 和風おみくじアプリ Version5 🎋</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">ボタンを押して、今日の運勢を楽しく占ってみましょう😊</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 「おみくじを引く」ボタン
# ---------------------------------------------------------
if st.button("✨ おみくじを引く ✨"):
    countdown_placeholder = st.empty()

    countdown_placeholder.markdown(
        """
        <div class="countdown-box">
            <div class="countdown-text">🎴 おみくじを振っています…</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.6)

    countdown_placeholder.markdown(
        """
        <div class="countdown-box">
            <div class="countdown-number">3</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.45)

    countdown_placeholder.markdown(
        """
        <div class="countdown-box">
            <div class="countdown-number">2</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.45)

    countdown_placeholder.markdown(
        """
        <div class="countdown-box">
            <div class="countdown-number">1</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.45)

    countdown_placeholder.markdown(
        """
        <div class="countdown-box">
            <div class="result-announcement">🌸 結果が出ました！ 🌸</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(0.5)

    countdown_placeholder.empty()

    result = draw_omikuji()
    kotowaza = draw_kotowaza()
    mission = draw_mission()
    lucky_score = get_lucky_score(result["rank"])
    rank = result["rank"]

    # おみくじ累計回数をGoogleスプレッドシートに記録
    counter_url = "https://script.google.com/macros/s/AKfycbzwB6t4S3rFJfuNfgdYPI7D6fcmmxVxYuNLjPiZjSNEi1fAcHcMfI3jtD0sMLTpU6rv/exec?action=increment"

    try:
        response = requests.get(counter_url, timeout=5)
        response.raise_for_status()

        count_data = response.json()
        total_count = count_data["count"]

    except Exception as e:
        st.error(f"カウンター取得エラー：{e}")
        total_count = None

    if total_count is not None:
        st.write(f"📊 今日のおみくじの回数: {total_count}回")
    else:
        st.write("📊 今日のおみくじの回数: 不明")

    # 結果に応じたアニメーション
    if "超大吉" in rank:
        st.balloons()
        st.success("🎊 超大吉！大当たりです！今日は特別にツイています！")
    elif "大吉" in rank:
        st.balloons()
    elif "凶" in rank:
        st.snow()

    # 見出し表示
    st.subheader("🎉 あなたのおみくじの結果は… 🎉")

    # 超大吉だけ特別デザイン
    if "超大吉" in rank:
        st.markdown(
            """
            <div class="jackpot-text">
                🌟 おめでとうございます！レアな「超大吉」を引き当てました！ 🌟
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="super-fortune-card">
                <div class="super-badge-wrap">
                    <div class="super-badge">🎯 RARE FORTUNE GET! 🎯</div>
                </div>
                <div class="super-fortune-rank">{result["rank"]}</div>
                <div class="super-fortune-message">{result["message"]}</div>
                <div class="super-fortune-detail">🎨 <b>ラッキーカラー：</b> {result["lucky_color"]}</div>
                <div class="super-fortune-detail">🔢 <b>ラッキーナンバー：</b> {result["lucky_number"]}</div>
                <div class="super-fortune-detail">🎁 <b>ラッキーアイテム：</b> {result["lucky_item"]}</div>
                <div class="score-title">⭐ 今日のラッキースコア</div>
                <div class="super-score-box">
                    <div class="super-score-number">{lucky_score}点 / 100点</div>
                    <div class="score-caption">今日は特に運気が高まっている一日です。</div>
                </div>
                <div class="advice-title">🌸 今日の開運アドバイス</div>
                <div class="super-advice-text">{result["advice"]}</div>
                <div class="kotowaza-title">📜 今日のラッキーことわざ</div>
                <div class="super-kotowaza-box">
                    <div class="kotowaza-quote">「{kotowaza["quote"]}」</div>
                    <div class="kotowaza-description">{kotowaza["description"]}</div>
                </div>
                <div class="mission-title">🎯 今日の開運ミッション</div>
                <div class="mission-box">
                <div class="mission-name">{mission["mission"]}</div>
                <div class="mission-description">{mission["description"]}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info("👑 超大吉はとても低い確率で出現する特別なおみくじです。まさに「当たり」ですね！")
    else:
        # 通常の結果カード
        st.markdown(
            f"""
            <div class="fortune-card">
                <div class="fortune-rank">{result["rank"]}</div>
                <div class="fortune-message">{result["message"]}</div>
                <div class="fortune-detail">🎨 <b>ラッキーカラー：</b> {result["lucky_color"]}</div>
                <div class="fortune-detail">🔢 <b>ラッキーナンバー：</b> {result["lucky_number"]}</div>
                <div class="fortune-detail">🎁 <b>ラッキーアイテム：</b> {result["lucky_item"]}</div>
                <div class="score-title">⭐ 今日のラッキースコア</div>
                <div class="score-box">
                    <div class="score-number">{lucky_score}点 / 100点</div>
                    <div class="score-caption">今日の運気の目安として、楽しくチェックしてみましょう。</div>
                </div>
                <div class="advice-title">🌸 今日の開運アドバイス</div>
                <div class="advice-text">{result["advice"]}</div>
                <div class="kotowaza-title">📜 今日のラッキーことわざ</div>
                <div class="kotowaza-box">
                    <div class="kotowaza-quote">「{kotowaza["quote"]}」</div>
                    <div class="kotowaza-description">{kotowaza["description"]}</div>
                </div>
                <div class="mission-title">🎯 今日の開運ミッション</div>
                <div class="mission-box">
                <div class="mission-name">{mission["mission"]}</div>
                <div class="mission-description">{mission["description"]}</div>
                </div>
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
    st.info("「✨ おみくじを引く ✨」ボタンを押すと、今日の運勢が表示されます。")
