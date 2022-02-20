from math import sqrt


tms_sce = {"1.90": {"0.81": "TMS-SCE-1K-3/32-2.0-9         2.36     0.79     0000154314"},
           "2.66": {"1.11": "TMS-SCE-1K-1/8-2.0-9          3.18     1.07     0000112634"},
           "4.06": {"1.75": "TMS-SCE-1K-3/16-2.0-9         4.75     1.57     0000130298"},
           "5.46": {"2.31": "TMS-SCE-1K-1/4-2.0-9          6.35     2.11     0000075442"},
           "8.12": {"3.47": "TMS-SCE-1K-3/8-2.0-9          9.53     3.18     0000152806"},
           "10.79": {"4.64": "TMS-SCE-1K-1/2-2.0-9          12.70    4.22     0000075440"},
           "16.25": {"6.99": "TMS-SCE-1K-3/4-2.0-9          19.05    6.35     0000138206"},
           "21.59": {"9.29": "TMS-SCE-1K-1-2.0-9            25.40    8.46     0000122084"},
           "33.02": {"20.95": "TMS-SCE-1K-1 1/2-2.0-9        38.10    19.05    0000486275"},
           "44.95": {"27.94": "TMS-SCE-1K-2-2.0-9            50.80    25.40    0000498999"},
           "50.80": {"22.32": "TMS-SCE-1K-2 1/4-2.0-9        57.15    19.05    0000153740"}}
tt_m_ng = {"3.99": {"2.1": "ТТ-М 4/2«Б»                   4        2        0000654330"},
           "5.99": {"3.1": "ТТ-М 6/3«Б»                   6        3        0000654331"},
           "9.99": {"5.1": "ТТ-М 10/5«Б»                  10       5        0000654332"},
           "11.99": {"6.1": "ТТ-М 12/6«Б»                  12       6        0000654333"},
           "3.98": {"2.1": "ТТ-М 4/2«Ж»                   4        2        0000654334"},
           "5.98": {"3.1": "ТТ-М 6/3«Ж»                   6        3        0000654335"},
           "9.98": {"5.1": "ТТ-М 10/5«Ж»                  10       5        0000654336"},
           "11.98": {"6.1": "ТТ-М 12/6«Ж»                  12       6        0000654337"}}


def main_calculation_diameter():
    choice = input("Хотите посчитать диаметр жгута в кабеле по ГОСТ 23586-96? (Да/Нет) ").lower().title()
    if choice == "Да":
        tmp_list = []
        wire_dict = {}
        name_parts = input(f"Введите наименование участка. (Например: Х1 - МР1, где МР1 - место разветвления 1): ")
        num_type_wire = int(input(f"Введите сколько различных типов проводов на участке {name_parts} (целое число): "))
        count_num_type_wire = 1
        while count_num_type_wire <= num_type_wire:
            diam_type_wire = float(input(f"Введите диаметр {count_num_type_wire} провода: ").replace(",", "."))
            count_type_wire = int(input(f"Введите количество {count_num_type_wire} провода (целое число): "))
            for i in range(count_type_wire):
                tmp_list.append(diam_type_wire)
            count_num_type_wire += 1
        wire_dict[name_parts] = {"Dср": round(sum(tmp_list) / len(tmp_list), 2), "n": len(tmp_list)}
        for i in wire_dict:
            d = round(1.3 * sqrt(wire_dict[i]["n"]) * wire_dict[i]["Dср"])
            wire_dict[i]["D"] = d
        tms_choice(wire_dict)
        tmp = input("Для выхода нажми 'ENTER'")
    else:
        print("Помни ОРЁЛ всегда следит за тобой из гнезда, свитого из возвращенных кабелЕй!!!)")
        tmp = input("Для выхода нажми 'ENTER'")


def tms_choice(wire_dict):
    for i in wire_dict:
        print(f"Подходящие трубки для участка {i}: "
              f"Dср = {wire_dict[i]['Dср']}мм, "
              f"n = {wire_dict[i]['n']}, "
              f"D = {wire_dict[i]['D']}мм "
              f"\n")
        print("Тип трубки                    MAX      MIN      Код PDM \n")
        for j in tms_sce:
            for k in tms_sce[j]:
                if float(k) < wire_dict[i]["D"] < float(j):
                    print(tms_sce[j][k])
        for j in tt_m_ng:
            for k in tt_m_ng[j]:
                if float(k) < wire_dict[i]["D"] < float(j):
                    print(tt_m_ng[j][k])
        print("\n")


if __name__ == '__main__':
    main_calculation_diameter()
