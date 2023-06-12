# %% 230321 v02
import os
import configparser


class Config():
    """
    Ex.
    data = {'DEFAULT': {'user': 'yj20_kim', 'Password': ''}}
    
    - initialize: make *.cfg with data (overwrite)
    - update: update and return data (if there is a file)
    - get_data: return data
    
    Note: [DEFAULT] section is included in [OTHER] sections
    
    -- READ/WRITE : *.cfg <-> self._data
    -- PROMT: self._data <- input()
    -- INITIALIZE: self._data <- dict_data
    """
    
    _file_path: str = ''
    _data: dict = {}

    
    def __init__(self, file_path='./login_info.cfg') -> None:
        self._file_path = file_path
        
    
    def update(self):
        # check init
        self._read()
        self._promt_all()
        self._write()
        
        return self._data
    
    def initialize(self, data: dict):
        config = configparser.ConfigParser()
        
        # check format
        config.read_dict(data)
        self._data = data
        self._write()
        
    def get_data(self):
        self._read()
        
        return self._data
    

    # def update_section_option_value(self):
    #     self._read()
    #     self._promt_all()
    #     self._write()
    # def check difference data vs *.cfg
    # def update_manual(self):
    
    def _promt_all(self):
        for s in self._data.keys():
            for o in self._data[s].keys():
                text = f"Change the value {s}.{o} = {self._data[s][o]}, or skip"
                print(text)
                self._data[s][o] = input(text) or self._data[s][o]
                print(f"{s}.{o} = {self._data[s][o]}")

    def _read(self) -> dict:
        config = configparser.ConfigParser()
        config.read_file(open(self._file_path))

        self._data = {s: {o: config[s][o] for o in config[s].keys()} for s in config.keys()}
        
        return self._data

    def _write(self):
        config = configparser.ConfigParser()
        config.read_dict(self._data)
        
        # check folder
        dir_path = os.path.dirname(self._file_path)
        if dir_path:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
    
        with open(self._file_path, 'w') as configfile:
            config.write(configfile)

    def has_none(self):
        self._read()
        for s in self._data.keys():
            for o in self._data[s].keys():
                if not self._data[s][o]:
                    return True
        return False


# %%
if __name__ == '__main__':
    cfg = Config('test/test.cfg')
    cfg.initialize({123: {234: 345, 789: ''}})
    
    print(cfg.has_none())
    ret = cfg.update()

    # update by manual
    ret = cfg.get_data()
