import speedtest
from tqdm import tqdm

def test_internet_speed():
    st = speedtest.Speedtest()
    
    print()
    print("最適なサーバーを選択中...")
    for _ in tqdm(range(10)):
        st.get_best_server()
    print()
        
    print("ダウンロード速度を測定中...")
    for _ in tqdm(range(10)):
        download_speed = st.download()
    print()
        
    print("アップロード速度を測定中...")
    for _ in tqdm(range(10)):
        upload_speed = st.upload()
    print()
    
    result_upload = upload_speed / 1024 / 1024
    result_download = download_speed / 1024 / 1024
        
    print("=" * 20 +"\n")
    print(f"ダウンロード速度: {int(result_download)} Mbps")
    print(f"アップロード速度: {int(result_upload)} Mbps")
    print()
    print(f"総合値: {int(result_download + result_upload)} pts")
    
    evaluation = None
    
    if result_download + result_upload >= 300:
        evaluation = "S"
    elif result_download + result_upload >= 200:
        evaluation = "A"
    elif result_download + result_upload >= 100:
        evaluation = "B"
    elif result_download + result_upload >= 50:
        evaluation = "C"
    else:
        evaluation = "D"
    print(f"評価: {evaluation}")
    print("\n" + "=" * 20)
    
if __name__ == "__main__":
    import sys
    test_internet_speed()
    
    retry = input("もう一度測定しますか？ (y/n): ")
    
    if retry.lower() == 'y':
        test_internet_speed()
    else:
        sys.exit(0)
    