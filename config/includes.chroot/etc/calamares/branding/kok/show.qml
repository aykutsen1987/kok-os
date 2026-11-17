import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation {
    id: presentation

    // Tüm alanı kaplayan koyu zemin (beyaz kenar kalmasın)
    Rectangle { anchors.fill: parent; color: "#0F2A47"; z: -10 }

    Timer { interval: 7000; running: true; repeat: true; onTriggered: presentation.goToNextSlide() }

    Slide {
        Rectangle { anchors.fill: parent
            gradient: Gradient { GradientStop { position: 0.0; color: "#1565C0" } GradientStop { position: 1.0; color: "#7B1FA2" } } }
        Rectangle { width: 280; height: 280; radius: 140; color: "#22FFFFFF"; x: parent.width - 190; y: -80 }
        Rectangle { width: 190; height: 190; radius: 95; color: "#18FFFFFF"; x: -60; y: parent.height - 130 }
        Column { anchors.centerIn: parent; width: parent.width - 100; spacing: 14
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 32; font.bold: true
                   text: "Kök OS'a hoş geldiniz" }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#E3EEFF"; font.pixelSize: 18
                   text: "Eski bilgisayarınıza yeni bir soluk." }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#B9CFF5"; font.pixelSize: 14
                   text: "Welcome to Kök OS – new life for your older computer." }
        }
    }

    Slide {
        Rectangle { anchors.fill: parent
            gradient: Gradient { GradientStop { position: 0.0; color: "#00796B" } GradientStop { position: 1.0; color: "#1B5E20" } } }
        Rectangle { width: 260; height: 260; radius: 130; color: "#22FFFFFF"; x: -70; y: -70 }
        Rectangle { width: 200; height: 200; radius: 100; color: "#18FFFFFF"; x: parent.width - 120; y: parent.height - 140 }
        Column { anchors.centerIn: parent; width: parent.width - 100; spacing: 14
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 32; font.bold: true
                   text: "Hafif ve akıcı" }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#E0F7EF"; font.pixelSize: 18
                   text: "Eski bilgisayarlarda bile hızlı açılır; bellek ve işlemci akıllıca kullanılır." }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#B5E3D3"; font.pixelSize: 14
                   text: "Light and smooth, even on older hardware." }
        }
    }

    Slide {
        Rectangle { anchors.fill: parent
            gradient: Gradient { GradientStop { position: 0.0; color: "#EF6C00" } GradientStop { position: 1.0; color: "#C62828" } } }
        Rectangle { width: 270; height: 270; radius: 135; color: "#22FFFFFF"; x: parent.width - 200; y: parent.height - 170 }
        Rectangle { width: 170; height: 170; radius: 85; color: "#18FFFFFF"; x: 40; y: -60 }
        Column { anchors.centerIn: parent; width: parent.width - 100; spacing: 14
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 32; font.bold: true
                   text: "Windows programları" }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#FFEBDD"; font.pixelSize: 18
                   text: ".exe dosyasına çift tıklayın, Windows programlarınız Kök OS'ta çalışsın." }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#FFD0B0"; font.pixelSize: 14
                   text: "Run your Windows programs with a double click." }
        }
    }

    Slide {
        Rectangle { anchors.fill: parent
            gradient: Gradient { GradientStop { position: 0.0; color: "#2E7D32" } GradientStop { position: 1.0; color: "#006064" } } }
        Rectangle { width: 250; height: 250; radius: 125; color: "#22FFFFFF"; x: -60; y: parent.height - 160 }
        Rectangle { width: 190; height: 190; radius: 95; color: "#18FFFFFF"; x: parent.width - 150; y: -50 }
        Column { anchors.centerIn: parent; width: parent.width - 100; spacing: 14
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 32; font.bold: true
                   text: "Android uygulamaları" }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#E2F6E4"; font.pixelSize: 18
                   text: "Telefon uygulamalarınızı bilgisayarınızda da kullanın." }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#B8E6C0"; font.pixelSize: 14
                   text: "Use your Android apps on the desktop." }
        }
    }

    Slide {
        Rectangle { anchors.fill: parent
            gradient: Gradient { GradientStop { position: 0.0; color: "#0D2A4A" } GradientStop { position: 1.0; color: "#1976D2" } } }
        Rectangle { width: 240; height: 240; radius: 120; color: "#22FFFFFF"; x: parent.width - 170; y: -60 }
        Rectangle { width: 200; height: 200; radius: 100; color: "#18FFFFFF"; x: -50; y: parent.height - 130 }
        Column { anchors.centerIn: parent; width: parent.width - 100; spacing: 14
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 32; font.bold: true
                   text: "Kurulum sürüyor" }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#DCEBFF"; font.pixelSize: 18
                   text: "Bu işlem birkaç dakika sürer. Lütfen bilgisayarı kapatmayın." }
            Text { width: parent.width; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "#A9C8F0"; font.pixelSize: 14
                   text: "Geliştirici / Developer: @aykutsen1987" }
        }
    }
}
