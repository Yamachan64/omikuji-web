import random

# おみくじの結果リスト（大吉から凶まで）
omikuji_results = ["🎉 大吉", "😊 中吉", "🙂 吉", "🍀 小吉", "😢 凶"]

print("🎋 おみくじを引きます！")

# ランダムに1つを選択して結果を表示
result = random.choice(omikuji_results)
print(result)
