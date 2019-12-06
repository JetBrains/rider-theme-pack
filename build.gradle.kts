plugins {
    id("org.jetbrains.intellij") version "0.4.13"
}

repositories {
    mavenCentral()
}

intellij {
    val BuildForIDEA = false
    if (BuildForIDEA) {
        version = "2019.3"
    } else {
        type = "RD"
        version = "2019.3-SNAPSHOT"
    }
    pluginName = "Rider UI Theme Pack"

    tasks {
        buildSearchableOptions {
            enabled = false
        }

        // Initially introduced in:
        // https://github.com/JetBrains/ForTea/blob/master/Frontend/build.gradle.kts
        withType<org.jetbrains.intellij.tasks.RunIdeTask> {
            // IDEs from SDK are launched with 512m by default, which is not enough for Rider.
            // Rider uses this value when launched not from SDK.
            maxHeapSize = "1500m"
        }
    }
}
