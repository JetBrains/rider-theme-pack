package com.jetbrains.riderThemePack

import com.intellij.DynamicBundle
import org.jetbrains.annotations.Nls
import org.jetbrains.annotations.PropertyKey
import java.util.function.Supplier

private const val BUNDLE = "messages.ThemesBundle"

object ThemesBundle : DynamicBundle(BUNDLE) {

    @JvmStatic
    @Nls
    fun message(@PropertyKey(resourceBundle = BUNDLE) key: String, vararg params: Any): String = getMessage(key, *params)

    @JvmStatic
    fun messagePointer(@PropertyKey(resourceBundle = BUNDLE) key: String,
                       vararg params: Any): Supplier<String> = getLazyMessage(key, *params)
}