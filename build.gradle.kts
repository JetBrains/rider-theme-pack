import org.jetbrains.intellij.platform.gradle.tasks.RunIdeTask

plugins {
    id("org.jetbrains.intellij.platform") version "2.6.0"
    id("me.filippov.gradle.jvm.wrapper") version "0.15.0"
}

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

version = "0.15.3"

val useRiderSdk = System.getProperty("useRiderSdk")?.toBoolean() ?: false
val useStableBuild = System.getProperty("useStableBuild")?.toBoolean() ?: false

dependencies {
    intellijPlatform {
        if (useRiderSdk) {
            if (useStableBuild) {
                rider("2025.1", useInstaller = false) // Rider release
            } else {
                rider("2025.2-SNAPSHOT", useInstaller = false) // Rider snapshot
            }
        } else {
            if (useStableBuild) {
                intellijIdeaCommunity("2025.1") // IDEA release
            } else {
                intellijIdeaCommunity("252.23892-EAP-CANDIDATE-SNAPSHOT", useInstaller = false) // IDEA snapshot
            }
        }
    }
}

intellijPlatform {
    pluginConfiguration {
        name.set("Rider UI Theme Pack")
    }
}

tasks {
    buildSearchableOptions {
        enabled = false
    }

    if (!useRiderSdk) {
        withType<RunIdeTask> {
            // IDEs from SDK are launched with 512m by default, which is not enough for Rider.
            // Rider uses this value when launched not from SDK.
            maxHeapSize = "1500m"
        }
    }
    patchPluginXml {
        sinceBuild.set(provider { null })
        untilBuild.set(provider { null })
    }
}
