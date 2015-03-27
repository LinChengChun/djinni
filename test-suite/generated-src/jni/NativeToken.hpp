// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from token.djinni

#pragma once

#include "djinni_support.hpp"
#include "token.hpp"

namespace djinni_generated {

class NativeToken final : djinni::JniInterface<::Token, NativeToken> {
public:
    using CppType = std::shared_ptr<::Token>;
    using JniType = jobject;

    static jobject toJava(JNIEnv* jniEnv, std::shared_ptr<::Token> c) { return djinni::JniClass<::djinni_generated::NativeToken>::get()._toJava(jniEnv, c); }
    static std::shared_ptr<::Token> fromJava(JNIEnv* jniEnv, jobject j) { return djinni::JniClass<::djinni_generated::NativeToken>::get()._fromJava(jniEnv, j); }

    const djinni::GlobalRef<jclass> clazz { djinni::jniFindClass("com/dropbox/djinni/test/Token") };

    class JavaProxy final : djinni::JavaProxyCacheEntry, public ::Token {
    public:
        JavaProxy(jobject obj);

    private:
        using djinni::JavaProxyCacheEntry::getGlobalRef;
        friend class djinni::JniInterface<::Token, ::djinni_generated::NativeToken>;
        friend class djinni::JavaProxyCache<JavaProxy>;
    };

private:
    NativeToken();
    friend class djinni::JniClass<::djinni_generated::NativeToken>;
};

}  // namespace djinni_generated