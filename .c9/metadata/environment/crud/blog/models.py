{"filter":false,"title":"models.py","tooltip":"/crud/blog/models.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":53},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":55},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":23,"column":53},"action":"insert","lines":["class Pet(models.Model):","\tavatar = models.ImageField(upload_to='pet')","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(100, 100)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션"],"id":56}],[{"start":{"row":18,"column":1},"end":{"row":18,"column":7},"action":"remove","lines":["avatar"],"id":58},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["i"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["m"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["a"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["g"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":24},"end":{"row":18,"column":43},"action":"remove","lines":["","\timage = models.ImageField(upload_to='pet')"],"id":59}],[{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"remove","lines":["1"],"id":60}],[{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"insert","lines":["2"],"id":61}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["1"],"id":62}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["2"],"id":63}],[{"start":{"row":17,"column":24},"end":{"row":22,"column":53},"action":"remove","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션"],"id":64}],[{"start":{"row":13,"column":4},"end":{"row":18,"column":53},"action":"insert","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션"],"id":65}],[{"start":{"row":18,"column":53},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":19,"column":0},"end":{"row":19,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":8},"action":"remove","lines":["    "],"id":67}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"remove","lines":[":"],"id":68}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":23},"action":"remove","lines":["","class Pet(models.Model)"],"id":69},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "]},{"start":{"row":21,"column":25},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":4},"end":{"row":19,"column":2},"action":"remove","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":70}],[{"start":{"row":13,"column":4},"end":{"row":19,"column":2},"action":"insert","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":71}],[{"start":{"row":13,"column":4},"end":{"row":19,"column":2},"action":"remove","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":72}],[{"start":{"row":15,"column":25},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]},{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":74}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["d"],"id":75},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["f"],"id":76},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["e"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["d"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":8},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":17,"column":0},"end":{"row":17,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "],"id":78},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["c"],"id":79},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["l"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["a"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["s"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["p"],"id":81},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["e"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["r"],"id":82},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["p"]}],[{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["t"],"id":83},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["h"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["u"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["m"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["n"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["a"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["i"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":[" "],"id":84}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"remove","lines":[" "],"id":85}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":16},"action":"insert","lines":["()"],"id":86}],[{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["m"],"id":87},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["o"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["d"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["e"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["l"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["s"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["."]},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["M"]}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["o"],"id":88},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["d"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["e"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"remove","lines":["s"],"id":89}],[{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["l"],"id":90}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":[":"],"id":91}],[{"start":{"row":17,"column":29},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":92},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":4},"end":{"row":24,"column":2},"action":"insert","lines":["","\timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":93}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":94}],[{"start":{"row":17,"column":29},"end":{"row":23,"column":2},"action":"remove","lines":["","    \timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":95}],[{"start":{"row":12,"column":53},"end":{"row":18,"column":2},"action":"insert","lines":["","    \timage_thumbnail = ImageSpecField(","\t\tsource = 'image', \t\t                    # 원본 ImageField 명","\t\tprocessors = [ResizeToFill(200, 200)],      # 사이즈 조정","\t\tformat = 'JPEG',\t\t                    # 최종 저장 포맷","\t\toptions = {'quality': 80})                  # 저장 옵션","\t\t"],"id":96}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":97},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["\t"],"id":98},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":99},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":100},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "],"id":101}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"insert","lines":["    "],"id":102}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":5},"action":"insert","lines":["    "],"id":103}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":104}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"insert","lines":["    "],"id":105}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":[" "],"id":106},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":[" "]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":[" "]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":107},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":108},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":109},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":110},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":111},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":112},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":113},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":114},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":115},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":116},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":117},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":118},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":119},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":120},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":121},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":122},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":123},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":17,"column":33},"action":"remove","lines":["\timage_thumbnail = ImageSpecField(","    source = 'image', \t\t                    # 원본 ImageField 명","    processors = [ResizeToFill(200, 200)],      # 사이즈 조정","    format = 'JPEG',\t\t                    # 최종 저장 포맷","    options = {'quality': 80})   "],"id":124}],[{"start":{"row":13,"column":0},"end":{"row":17,"column":36},"action":"insert","lines":["photo_thumbnail = ImageSpecField(","\t\tsource = 'photo', \t\t   # 원본 ImageField 명","\t\tprocessors = [Thumbnail(100, 100)], # 처리할 작업목록","\t\tformat = 'JPEG',\t\t   # 최종 저장 포맷","\t\toptions = {'quality': 60}) # 저장 옵션"],"id":125}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":29},"action":"remove","lines":["class thumnail(models.Model):"],"id":126}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":127}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":17},"action":"remove","lines":["photo"],"id":128},{"start":{"row":14,"column":12},"end":{"row":14,"column":17},"action":"insert","lines":["image"]}],[{"start":{"row":2,"column":44},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":129}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":41},"action":"insert","lines":["from imagekit.processors import Thumbnail"],"id":130}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":58},"action":"remove","lines":["              # 저장 옵션"],"id":131},{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":[" "],"id":132}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":30},"action":"insert","lines":["    "],"id":133}],[{"start":{"row":15,"column":30},"end":{"row":15,"column":34},"action":"insert","lines":["    "],"id":134}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":38},"action":"insert","lines":["    "],"id":135}],[{"start":{"row":15,"column":38},"end":{"row":15,"column":42},"action":"insert","lines":["    "],"id":136}],[{"start":{"row":15,"column":42},"end":{"row":15,"column":46},"action":"insert","lines":["    "],"id":137}],[{"start":{"row":16,"column":38},"end":{"row":16,"column":42},"action":"insert","lines":["    "],"id":138}],[{"start":{"row":16,"column":42},"end":{"row":16,"column":46},"action":"insert","lines":["    "],"id":139}],[{"start":{"row":16,"column":46},"end":{"row":16,"column":50},"action":"insert","lines":["    "],"id":140}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":[" "],"id":141}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":28},"action":"insert","lines":["    "],"id":142}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":32},"action":"insert","lines":["    "],"id":143}],[{"start":{"row":17,"column":32},"end":{"row":17,"column":36},"action":"insert","lines":["    "],"id":144}],[{"start":{"row":17,"column":36},"end":{"row":17,"column":40},"action":"insert","lines":["    "],"id":145}],[{"start":{"row":17,"column":40},"end":{"row":17,"column":44},"action":"insert","lines":["    "],"id":146}],[{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":[" "],"id":147}],[{"start":{"row":18,"column":30},"end":{"row":18,"column":34},"action":"insert","lines":["    "],"id":148}],[{"start":{"row":18,"column":34},"end":{"row":18,"column":38},"action":"insert","lines":["    "],"id":149}],[{"start":{"row":18,"column":38},"end":{"row":18,"column":42},"action":"insert","lines":["    "],"id":150}],[{"start":{"row":18,"column":42},"end":{"row":18,"column":46},"action":"insert","lines":["    "],"id":151}],[{"start":{"row":18,"column":46},"end":{"row":18,"column":50},"action":"insert","lines":["    "],"id":152}],[{"start":{"row":1,"column":47},"end":{"row":2,"column":44},"action":"remove","lines":["     ","from imagekit.processors import ResizeToFill"],"id":153},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"remove","lines":[" "]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"remove","lines":[" "]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"remove","lines":[" "]},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"remove","lines":[" "]},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":[" "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":4},"end":{"row":13,"column":19},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1595057502111,"hash":"6f4ff854c881c18b17adead7370adbe3fb9a2d3b"}