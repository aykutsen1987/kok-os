import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation {
    id: presentation
    Timer { interval: 6000; running: true; repeat: true; onTriggered: presentation.goToNextSlide() }


    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 26
               text: "Kök OS'a hoş geldiniz\n\nEski bilgisayarınıza yeni bir soluk." }
    }
    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 24
               text: "Windows programları (.exe) ve Android uygulamaları (.apk) tek sistemde." }
    }
    Slide {
        Rectangle { anchors.fill: parent; color: "#1B1F2A" }
        Text { anchors.centerIn: parent; width: parent.width-80; horizontalAlignment: Text.AlignHCenter; wrapMode: Text.WordWrap; color: "white"; font.pixelSize: 24
               text: "Tamamen Türkçe, hafif ve akıcı.\n\nKurulum birkaç dakika içinde tamamlanacak." }
    }
}
