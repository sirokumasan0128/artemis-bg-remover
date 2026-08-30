import customtkinter as ctk

# デザインテーマ設定: ダークモードを強制適用（Artemisの深宇宙・月光デザイン）
ctk.set_appearance_mode("Dark")

# Artemis 宇宙・月光風プレミアムカラーパレット（ダーク専用）の定義
C_BG = "#0A0A0E"           # メイン背景（深宇宙の漆黒）
C_PANEL = "#12121A"        # カード・パネル背景（星雲を想起させるディープネイビーパープル）
C_CARD = "#1A1A26"         # 内部カード背景（パネルより少し明るい）
C_TEXT = "#F1F5F9"         # 主要テキスト（ムーンホワイト）
C_TEXT_LIGHT = "#94A3B8"   # サブテキスト

C_PRIMARY = "#818CF8"      # Artemis月光ブルー/インディゴ（プライマリアクション）
C_PRIMARY_HOVER = "#6366F1"

C_SECONDARY = "#1E1B4B"    # セカンダリアクション
C_SECONDARY_HOVER = "#312E81"

C_ACCENT = "#38BDF8"       # ムーンアクセント（シアン / ライトスカイブルー）
C_ACCENT_HOVER = "#0EA5E9"

C_DANGER = "#F87171"       # 警告・削除アクション
C_DANGER_HOVER = "#EF4444"

# --- 機能別カラー（月の女神の神秘性を保ちつつ、カテゴリを識別する星座色） ---
C_SUCCESS = "#34D399"        # 完了・成功（エメラルドグリーン：オーロラの輝き）
C_SUCCESS_HOVER = "#10B981"
C_PURPLE = "#C084FC"         # アバター関連（ムーンパープル：月明かりの幻想）
C_PURPLE_HOVER = "#A855F7"
C_AMBER = "#FCD34D"          # 警告・ハイライト（スターゴールド：流れ星の軌跡）
C_AMBER_HOVER = "#F59E0B"
C_TEAL = "#2DD4BF"           # BGM関連（スターダストティール：天の川の青碧）
C_TEAL_HOVER = "#14B8A6"

# --- フォント定数（一貫したタイポグラフィ） ---
FONT_TITLE = ("Georgia", 26, "bold", "italic")   # アプリタイトル
FONT_HEADING = ("Helvetica", 14, "bold")          # セクション見出し
FONT_SUBHEADING = ("Helvetica", 12, "bold")       # サブ見出し
FONT_BODY = ("Helvetica", 12)                     # 本文
FONT_CAPTION = ("Helvetica", 11)                  # キャプション・ラベル
FONT_CAPTION_BOLD = ("Helvetica", 11, "bold")     # 強調ラベル
FONT_MONO = ("Courier", 13)                       # ログ・コード

# --- カード・レイアウト定数 ---
CARD_RADIUS = 12       # 外部カードの角丸
CARD_INNER_RADIUS = 8  # 内部カードの角丸
CARD_PAD_X = 15        # カード内水平パディング
CARD_PAD_Y = 10        # カード内垂直パディング
