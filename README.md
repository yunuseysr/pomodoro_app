# Pomodoro Sayacı Uygulaması

Bu basit Pomodoro sayacı uygulaması, çalışma ve ara sürelerini yönetmekte ve günlük Pomodoro sayısını izlemektedir. Pomodoro tekniği, belirli bir süre boyunca konsantre olmanızı ve ardından kısa bir ara vermenizi sağlayarak verimliliği artırmak için kullanılır.

## Kullanım

1. Uygulamayı başlatın (`main.py` dosyasını çalıştırarak).
2. Çalışma süresini ve ara süresini dakika cinsinden girin. Varsayılan süreler 25 dakika çalışma ve 5 dakika aradır.
3. "Başla" düğmesine tıklayarak Pomodoro seansını başlatın.
4. "Durdur" düğmesiyle seansı durdurabilir ve "Devam Et" düğmesiyle tekrar devam edebilirsiniz.
5. Pomodoro seansını tamamladığınızda "Bitir" düğmesine tıklayarak tamamlayabilirsiniz.
6. Uygulama, toplam tamamlanan Pomodoro sayısını gösterir.

## Gereksinimler

- Python 3.x
- PyQt5 kütüphanesi (gerekli bağımlılıkları yüklemek için `requirements.txt` dosyasını kullanabilirsiniz)

## Kurulum

1. Python 3.x yüklü olmalıdır. Yüklü değilse [Python web sitesinden indirebilirsiniz](https://www.python.org/downloads/).
2. Gerekli bağımlılıkları yüklemek için terminalde aşağıdaki komutu kullanın:
   
```bash
pip install -r requirements.txt
```

## Nasıl Çalıştırılır

Bu Pomodoro uygulamasını iki farklı şekilde çalıştırabilirsiniz.

### 1. Terminal Üzerinden

Projenin ana dizinine gidin ve aşağıdaki adımları izleyin:

1. Terminali açın.

2. Aşağıdaki komutu girin:

    ```bash
    python3 main.py
    ```

3. Uygulama çalışacak ve Pomodoro sayacı arayüzü görüntülenecektir.

### 2. Çalıştırılabilir Uygulama Olarak

1. Projenin ana dizinine gidin.

2. Terminalde aşağıdaki komutları sırasıyla çalıştırarak `main.py` dosyasına çalıştırma izni verin:

    ```bash
    chmod +x main.py
    ```

3. Uygulamayı doğrudan adıyla terminalden çalıştırabilirsiniz:

    ```bash
    ./main.py
    ```

4. Pomodoro sayacı uygulaması görüntülenecektir. Çalışma ve ara sürelerini girip "Başla" düğmesine tıklayarak Pomodoro seansını başlatabilirsiniz.

5. Seansı tamamladığınızda "Bitir" düğmesine tıklayarak tamamlayabilirsiniz.

6. Uygulamayı kapatmak için pencereyi kapatın veya terminalde `Ctrl + C` tuş kombinasyonunu kullanın.

Uygulamanın nasıl kullanılacağı hakkında daha fazla bilgi için [Pomodoro Sayacı Uygulaması](#pomodoro-sayacı-uygulaması) bölümüne göz atabilirsiniz.

