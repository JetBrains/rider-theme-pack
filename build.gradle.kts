plugins {
    id("org.jetbrains.intellij") version "1.15.0"
    id("me.filippov.gradle.jvm.wrapper") version "0.14.0"
}

repositories {
    mavenCentral()
}

version = "0.15.2"

intellij {
    val useRiderSdk = System.getProperty("useRiderSdk")?.toBoolean() ?: false
    val useStableBuild = System.getProperty("useStableBuild")?.toBoolean() ?: false
    if (useRiderSdk) {
        type.set("RD")
        if (useStableBuild) {
            version.set("2024.2.7") // Rider release
        }
        else {
            version.set("2024.3-SNAPSHOT") // Rider snapshot
        }
    }
    else {
        if (useStableBuild) {
            version.set("2024.2.4") // IDEA release
        }
        else {
            version.set("243.21565-EAP-CANDIDATE-SNAPSHOT") // IDEA snapshot
        }
    }

    pluginName.set("Rider UI Theme Pack")

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
            updateSinceUntilBuild.set(false)
//            sinceBuild.set("")
//            untilBuild.set("")
        }
    }
}
