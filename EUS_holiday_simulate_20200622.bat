rem 日中から入庫シミュレーション　日曜
py .\EUS_main.py 23 24 0.1 3

rem 朝から入庫シミュレーション　月曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 23 24 0.1 0

rem 朝から入庫シミュレーション　火曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 23 24 0.1 0

rem 朝から入庫シミュレーション　水曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 23 24 0.1 0

rem 朝から入庫シミュレーション　木曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 23 24 0.1 0

rem 朝から入庫シミュレーション　金曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 23 24 0.1 0

rem 朝から入庫シミュレーション　土曜
copy save\depot_save.json  save\depot_load.json
py .\EUS_main.py 11 12 0.1 1
pause
