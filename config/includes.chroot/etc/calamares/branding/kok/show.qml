import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation {
    id: presentation
    Timer { interval: 6000; running: true; repeat: true; onTriggered: presentation.goToNextSlide() }

    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 24
               text: "Kök OS'a hoş geldiniz\nWelcome to Kök OS\n\nEski bilgisayarınıza yeni bir soluk.\nNew life for your older computer." }
    }
    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 22
               text: "Windows programları (.exe) ve Android uygulamaları (.apk) tek sistemde.\nWindows programs (.exe) and Android apps (.apk) in one system." }
    }
    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 22
               text: "Türkçe veya İngilizce, hafif ve akıcı.\nTurkish or English, light and smooth.\n\nGeliştirici / Developer: @aykutsen1987" }
    }
}
