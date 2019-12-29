import subprocess
import platform
import random


class IOSInfo(object):

    def __init__(self):
        pass

    def collect(self):
        cmd = 'sw_vers'
        res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        result = res.stdout.read().decode()
        print(result)
        data_list = result.split('\n')
        print(data_list)
        data = dict()
        data['asset_type'] = 'server'
        data['manufacturer'] = 'Apple'
        print(platform.platform())
        data['os_type'] = platform.system()
        data['os_release'] = platform.platform()
        data['os_distribution'] = 'Apple'
        data.update(self.get_cpu_info())
        data.update(self.get_ram_info())
        data.update(self.get_motherboard_info())
        data.update(self.get_disk_info())
        data.update(self.get_nic_info())
        print(data)
        return data

    def get_cpu_info_by_cmd(self, cmd):
        res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        result = res.stdout.read().decode()

        return result.split(":")[1].strip()

    def get_cpu_info(self):
        """
        获取CPU的相关数据，这里只采集了三个数据，实际有更多，请自行选择需要的数据
        :return:
        """
        cmd = "/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Total Number of Cores'"

        cpu_core_count = self.get_cpu_info_by_cmd(cmd)
        cpu_count_cmd = "/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Number of Processors'"

        cpu_count = self.get_cpu_info_by_cmd(cpu_count_cmd)
        cpu_model_cmd = "/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Processor Name:'"
        cpu_model = self.get_cpu_info_by_cmd(cpu_model_cmd)

        data = {}
        print(cpu_count)
        print(cpu_model)
        print(cpu_core_count)

        data["cpu_count"] = cpu_count  # CPU个数
        data["cpu_model"] = cpu_model
        data["cpu_core_count"] = cpu_core_count  # CPU总的核数

        return data

    def get_ram_info(self):
        """
        收集内存信息
        :return:
        """
        data = []
        r = random.sample('abcdefghijklmnopqrstuvwxyz', 6)
        item_data = {
            "slot": 'slot 0',
            "capacity": 16,
            "model": 'LPDDR3',
            "manufacturer": 'samsung',
            "sn": '550' + ''.join(r)
        }
        data.append(item_data)  # 将每条内存的信息，添加到一个列表里

        return {"ram": data}  # 再对data列表封装一层，返回一个字典，方便上级方法的调用

    def get_motherboard_info(self):
        """
                获取主板信息
                :return:
                """
        r = random.sample('abcdefghijklmnopqrstuvwxyz', 6)
        data = {}
        data['computer_info'] = "apppls's motherboard"
        data['system_info'] = "apples's bios"

        data['manufacturer'] = 'apple'
        data['model'] = "apple's model"
        data['wake_up_type'] = "auto"
        data['sn'] = "motherboard_sn" + ''.join(r)
        return data

    def get_disk_info(self):
        """
        硬盘信息
        :return:
        """
        data = []
        r = random.sample('abcdefghijklmnopqrstuvwxyz', 6)
        disk_data = {}
        disk_data['interface_type'] = 'SCSI'

        disk_data['slot'] = '1'
        disk_data['sn'] = 'disksn' + ''.join(r)
        disk_data['model'] = 'disk.Model'
        disk_data['manufacturer'] = 'disk.Manufacturer'
        disk_data['capacity'] = '500G'
        data.append(disk_data)

        return {'physical_disk_driver': data}


    def get_nic_info(self):
        """
        网卡信息
        :return:
        """
        data = []

        nic_data = {}
        nic_data['mac'] = 'nic.MACAddress'
        nic_data['model'] = 'nic.Caption'
        nic_data['name'] = 'nic.Index'
        nic_data['ip_address'] = '127.0.0.1'
        nic_data['net_mask'] = '255.255.255.0'
        data.append(nic_data)

        return {'nic': data}

if __name__ == "__main__":
    i = IOSInfo()
    i.collect()
