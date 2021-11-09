# sinogram-generator

CT再構成で用いる透過像のデータ生成用ファイル

### Settingファイル
- setting.ymlを生成する.
    ```
    sphere_c: # 球の位置
    sphere_start: # 球のスタートの半径
    sphere_end: # 球の終わりの半径
    x_ray: [0, 0, 0] # X線源の位置
    detecta_sdd_x: 1500 # 検出器までのキョリ
    detecta_w: 1024 # 検出器の横幅
    detecta_h: 1024 # 検出器の縦幅
    projection_num: 1000 # 投影枚数
    output_path: 'dir-name' # 出力するDir
    ```

## projection image to sinogram
1. create projection image directory
2. run code
    ```
    $ python ./projection_to_sino.py -f ./lobster-1projection/lobster-sino-31744_32768-float32_1024x1024x1024.raw -o ./lobster-1sinogram/lobster-31744_32768-uint16 
    ```

# Rawデータのファイル分け

連続してスキャンされたデータを1Frameごとにまとめるファイル

## 対象ファイル
```
$ python devide_raw.py
```
