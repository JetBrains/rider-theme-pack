plugins {
    id("org.jetbrains.intellij") version "0.7.3"
    id("me.filippov.gradle.jvm.wrapper") version "0.9.3"
}

repositories {
    mavenCentral()
}

version = "0.9.1"

intellij {
    val useRiderSdk = System.getProperty("useRiderSdk")?.toBoolean() ?: false
    if (useRiderSdk) {
        type = "RD"
        //version = "2020.3-SNAPSHOT" // to run in Rider
        version = "2021.1.0" // release
    }
    else {
        //version = "203-SNAPSHOT" // to run in IDEA
        version = "2021.1" // release
    }

    pluginName = "Rider UI Theme Pack"

    tasks {
        buildSearchableOptions {
            enabled = false
        }

        // Initially introduced in:
        // https://github.com/JetBrains/ForTea/blob/master/Frontend/build.gradle.kts
        if (!useRiderSdk) {
            withType<org.jetbrains.intellij.tasks.RunIdeTask> {
                // IDEs from SDK are launched with 512m by default, which is not enough for Rider.
                // Rider uses this value when launched not from SDK.
                maxHeapSize = "1500m"
            }
        }
        withType<org.jetbrains.intellij.tasks.PatchPluginXmlTask> {
            updateSinceUntilBuild = true
            setUntilBuild("")
        }
    }
}
