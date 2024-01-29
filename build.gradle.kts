plugins {
    id("org.jetbrains.intellij") version "1.15.0"
    id("me.filippov.gradle.jvm.wrapper") version "0.14.0"
}

repositories {
    mavenCentral()
}

version = "0.14.11"

intellij {
    val useRiderSdk = System.getProperty("useRiderSdk")?.toBoolean() ?: false
    if (useRiderSdk) {
        type.set("RD")
        // version.set("2022.2-SNAPSHOT") // to run in Rider
        version.set("2023.3") // release
    }
    else {
        // version.set("222-SNAPSHOT") // to run in IDEA
        version.set("2023.3") // release
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
