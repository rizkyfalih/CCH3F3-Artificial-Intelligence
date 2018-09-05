class Fuzzy:
    def __init__(self, emosi, provokasi):
        self.nEmosi = []
        self.sEmosi = []
        self.nProvokasi = []
        self.sProvokasi = []
        self.hasilYa = []
        self.hasilTidak = []
        self.emosi = emosi
        self.provokasi = provokasi

    def cekEmosi(self):
        data = self.emosi
        if (data >= 0 and data <=37) :
            self.sEmosi.append("Rendah")
            self.nEmosi.append(1.0)
            self.sEmosi.append("Rendah")
            self.nEmosi.append(1.0)
        elif (data > 37 and data <= 39) :
            self.sEmosi.append("Rendah")
            self.nEmosi.append(-(data-39.0)/(39.0-37.0))
            self.sEmosi.append("Sedang")
            self.nEmosi.append((data-37.0)/(39.0-37.0))
        elif (data > 39 and data <= 61) :
            self.sEmosi.append("Sedang")
            self.nEmosi.append(1.0)
            self.sEmosi.append("Sedang")
            self.nEmosi.append(1.0)
        elif (data > 61 and data <= 64) :
            self.sEmosi.append("Sedang")
            self.nEmosi.append(-(data-64.0)/(64.0-61.0))
            self.sEmosi.append("Tinggi")
            self.nEmosi.append((data-61.0)/(64.0-61.0))
        elif (data > 64 and data <= 100) :
            self.sEmosi.append("Tinggi")
            self.nEmosi.append(1.0)
            self.sEmosi.append("Tinggi")
            self.nEmosi.append(1.0)
    
    def cekProfokasi(self) :
        data = self.provokasi
        if (data >= 0 and data <= 25):
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Rendah")
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Rendah")
        elif (data > 25 and data <= 31) :
            self.nProvokasi.append(-(data-31.0)/(31.0-25.0))
            self.sProvokasi.append("Rendah")
            self.nProvokasi.append((data-25.0)/(31.0-25.0))
            self.sProvokasi.append("Sedang")
        elif (data > 31 and data <= 50) :
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Sedang")
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Sedang")
        elif (data > 50 and data <= 61) :
            self.nProvokasi.append(-(data-61.0)/(61.0-50.0))
            self.sProvokasi.append("Sedang")
            self.nProvokasi.append((data-50.0)/(61.0-50.0))
            self.sProvokasi.append("Tinggi")
        elif (data > 61 and data <= 85) :
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Tinggi")
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Tinggi")
        elif (data > 85 and data <= 88) :
            self.nProvokasi.append(-(data-88.0)/(88.0-85.0))
            self.sProvokasi.append("Tinggi")
            self.nProvokasi.append((data-85.0)/(88.0-85.0))
            self.sProvokasi.append("Sangat Tinggi")
        elif (data > 88 and data <= 100) :
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Sangat Tinggi")
            self.nProvokasi.append(1.0)
            self.sProvokasi.append("Sangat Tinggi")

    def inference (self):
        for iE in range(0,2):
            for iP in range(0,2):
                if (self.sEmosi[iE] == 'Rendah' and self.sProvokasi[iP] == 'Rendah'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Rendah' and self.sProvokasi[iP] == 'Sedang'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Rendah' and self.sProvokasi[iP] == 'Tinggi'):
                    sHoax = 'Ya'
                if (self.sEmosi[iE] == 'Rendah' and self.sProvokasi[iP] == 'Sangat Tinggi'):
                    sHoax = 'Ya'
                if (self.sEmosi[iE] == 'Sedang' and self.sProvokasi[iP] == 'Rendah'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Sedang' and self.sProvokasi[iP] == 'Sedang'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Sedang' and self.sProvokasi[iP] == 'Tinggi'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Sedang' and self.sProvokasi[iP] == 'Sangat Tinggi'):
                    sHoax = 'Ya'
                if (self.sEmosi[iE] == 'Tinggi' and self.sProvokasi[iP] == 'Rendah'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Tinggi' and self.sProvokasi[iP] == 'Sedang'):
                    sHoax = 'Tidak'
                if (self.sEmosi[iE] == 'Tinggi' and self.sProvokasi[iP] == 'Tinggi'):
                    sHoax = 'Ya'
                if (self.sEmosi[iE] == 'Tinggi' and self.sProvokasi[iP] == 'Sangat Tinggi'):
                    sHoax = 'Ya'
                nHoax = min(self.nEmosi[iE], self.nProvokasi[iP])
                if (sHoax == 'Tidak') :
                    self.hasilTidak.append([nHoax, sHoax])
                else :
                    self.hasilYa.append([nHoax, sHoax])
        if (len(self.hasilYa) == 0) :
            self.hasilYa.append([0.0, "Ya"])
        if (len(self.hasilTidak) == 0) :
            self.hasilTidak.append([0.0, "Tidak"])

    def deffuzification(self):
        self.hasilTidak
        self.hasilYa
        ya = self.hasilTidak[0][0]
        tidak = self.hasilYa[0][0]
        yStar = ((ya*50.0 + tidak*100.0)/(ya+tidak))
        return yStar

    def cekHoax(self):
        if (self.deffuzification() > 50) :
            return 'Ya'
        else :
            return 'Tidak'

    def main(self):
        self.cekEmosi()
        self.cekProfokasi()
        self.inference()
        self.deffuzification()
        return str(self.emosi) + ' | ' + str(self.provokasi) + ' | '  + str(self.cekHoax())

eSample = [97, 36, 63, 82, 71, 79, 55, 57, 40, 57, 77, 68, 60, 82, 40, 80, 60, 50, 100, 11]
pSample = [74, 85, 43, 90, 25, 81, 62, 45, 65, 45, 70, 75, 70, 90, 85, 68, 72, 95, 18, 99]
eTest = [58, 68, 64, 57, 77, 98, 91, 50, 95, 27]
pTest = [63, 70, 66, 77, 55, 64, 59, 95, 55, 79]

for data in range(len(eSample)) :
    fuzzying = Fuzzy(eSample[data], pSample[data])
    print (str(data+1) + ' | ' + fuzzying.main())

for data in range(len(eTest)) :
    fuzzying = Fuzzy(eTest[data], pTest[data])
    print (str(data+21) + ' | ' + fuzzying.main())